from file_utils import get_whitelist_file, get_players_file
from player_database_connector import PlayerDatabase


def get_donor_uuids():
    donor_list = []

    player_json = get_players_file()

    for player in player_json["players"]:
        donor = player.get("donor")

        if donor:
            donor_list.append(player["UUID"])

    return donor_list


def get_donor_player_list():
    donors = []

    try:
        # Get list of donor uuids from database
        db = PlayerDatabase()
        db_connection = db.database.connection
        db_cursor = db_connection.cursor()
        db_cursor.execute("SELECT uuid.uuid FROM uuid INNER JOIN player_data pd on uuid.id = pd.uuid WHERE vip=true")

        uuids = db_cursor.fetchall()

        # Kall, Koenn, and our alts
        blacklist_uuids = ["b9be5135-fe8c-4a34-9e63-ffeef0fc80fb",
                           "cac04f5f-726f-4192-8290-24bdd9e7c9aa",
                           "90fd7b3f-239f-4ba4-809c-427081ebfa4e",
                           "0d594da7-6b81-463e-a0a7-d21c2e6b76f5"]

        for uuidTuple in uuids:
            uuid = uuidTuple[0].decode()

            # If player is not blacklisted
            if not blacklist_uuids.__contains__(uuid):

                # Add player to list of donors
                player_dict = {"username": db.get_name_from_uuid(uuid), "headImage": "https://visage.surgeplay.com/head/" + uuid}

                donors.append(player_dict)
        return donors
    except Exception as e:
        print("A problem occurred accessing the donors list. " + str(e))
        return None
