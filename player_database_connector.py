import re

from config import playerLocalDbName, playerLocalDbPassword, playerLocalDbURL, playerDevDbPassword, \
    playerLocalDbUsername, playerDevDbUsername, playerDevDbName, playerDevDbURL, playerDbDefaultServer
from database import Database
from remote_server_utils import check_on_hogwarts


class Server(object):
    def __init__(self, server_id, server_name):
        self.sqlId = server_id,
        self.name = server_name
        self.players = []

    def get_sql_id(self):
        return self.sqlId[0]


class Statistic(object):
    def __init__(self, id, name, count, level):
        self.id = id
        self.name = name,
        self.level = level,
        self.count = count

    def get_statistic_name(self):
        name = self.name[0]
        name = name.replace("_", " ")

        return name.title().strip()

    def get_statistic_level(self):
        return int(self.level[0])


class Player(object):
    def __init__(self, player_id, uuid, name):
        self.sqlId = player_id
        self.uuid = uuid
        self.statistics = []
        self.name = name
        self.total_score = 0


class PlayerDatabase(object):
    def __init__(self):
        if check_on_hogwarts():
            self.database = Database(playerLocalDbURL, playerLocalDbUsername, playerLocalDbPassword, playerLocalDbName)
        else:
            self.database = Database(playerDevDbURL, playerDevDbUsername, playerDevDbPassword, playerDevDbName)

        self.seasons = self.get_all_seasons_statistics()

    def get_sql_id_from_uuid(self, uuid):
        uuid_str = "'" + str(uuid) + "'"
        sql_id = self.database.execute_query("SELECT id FROM uuid WHERE uuid=" + uuid_str)

        return str(sql_id[0][0])

    @staticmethod
    def assign_player_scores(players):
        for player in players:
            total_score = 0
            for statistic in player.statistics:
                total_score += statistic.get_statistic_level()

            player.total_score = total_score

    def get_name_from_uuid(self, uuid):
        name = self.database.execute_query(
            "SELECT username, nickname FROM player_data WHERE uuid=" + self.get_sql_id_from_uuid(uuid))
        name = name[0]

        # Return nickname if it is present
        if name[1]:
            return name[1]
        else:
            return name[0]

    # Return the season with the matching id from the seasons list
    def get_season_from_list(self, id):
        for season in self.seasons:
            if season.get_sql_id() == int(id):
                return season

    # Return a list of Server objects with all the seasons named vanilla, that have statistics, WITHOUT PLAYER
    # INFORMATION
    def get_all_vanilla_seasons(self):
        seasons = []

        season_table = self.database.execute_query("SELECT * FROM server")

        for season in season_table:

            if str(season[1]).startswith("vanilla"):
                season_id = str(season[0])
                season_name = format_vanilla_server_name(season[1])

                # Append server if it has statistics
                statistic_table = self.database.execute_query("SELECT * FROM statistic_data WHERE server=" + season_id)
                if statistic_table:
                    seasons.append(Server(server_id=season_id, server_name=season_name))

        return seasons

    # Returns the name of the statistic of the given id
    def get_statistic_name_from_id(self, id):
        sql_name = self.database.execute_query("SELECT name FROM statistic WHERE id=" + str(id))[0][0]
        return sql_name

    # Returns the season of the given id's information as json
    def get_season_stats_json(self, season):
        season = self.get_season_from_list(season)

        json_players = []
        for player in season.players:
            json_statistics = []

            for statistic in player.statistics:
                # Add statistic if it is at least level 1
                if statistic.get_statistic_level() > 0:
                    json_statistic = {
                        "name": statistic.get_statistic_name(),
                        "level": statistic.get_statistic_level(),
                        "count": statistic.count
                    }
                    json_statistics.append(json_statistic)

            # Add player if they have at least 1 statistic over level 1
            if json_statistics:
                json_player = {
                    "uuid": player.uuid,
                    "name": player.name,
                    "statistics": json_statistics,
                    "score": player.total_score
                }
                json_players.append(json_player)

        season_json = {
            "name": season.name,
            "players": sorted(json_players, key=lambda k: k["score"], reverse=True)
        }

        return season_json

    def get_all_seasons_statistics(self):
        statistics_table = self.database.execute_query("SELECT * FROM statistic_data")

        seasons = []
        for statistic_item in statistics_table:
            server_id = int(statistic_item[2])

            # Get the relevant server object, or create one if this server doesnt have an object yet
            seasonObj = None
            for season in seasons:
                if season.get_sql_id() == server_id:
                    seasonObj = season
            if not seasonObj:
                server_name = self.database.execute_query("SELECT name FROM server WHERE id=" + str(server_id))
                seasonObj = Server(server_id, format_vanilla_server_name(str(server_name[0])))
                seasons.append(seasonObj)

            player_id = int(statistic_item[0])

            # Get the relevant player object, or create one if this player doesnt have an object yet
            playerObj = None
            for player in seasonObj.players:
                if player.sqlId == player_id:
                    playerObj = player
            if not playerObj:
                uuid = self.database.execute_query("SELECT uuid FROM uuid WHERE id=" + str(player_id))[0]
                playerObj = Player(player_id, uuid[0], self.get_name_from_uuid(uuid[0]))
                seasonObj.players.append(playerObj)

            # Add this statistic to the player
            statistic_id = int(statistic_item[1])
            playerObj.statistics.append(Statistic(statistic_id, self.get_statistic_name_from_id(statistic_id),
                                                  str(statistic_item[3]), str(statistic_item[4])))

        for season in seasons:
            self.assign_player_scores(season.players)

        return seasons

    def get_top_3(self):
        # Get the current season
        season = self.get_season_from_list(playerDbDefaultServer)

        # Sort by score
        players = sorted(season.players, key=lambda k: k.total_score, reverse=True)

        # Return the top 3
        return players[0], players[1], players[2]


def format_vanilla_server_name(name):
    return "Season " + re.sub("[^0-9]", "", name)
