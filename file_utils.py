import json

PLAYERS_JSON_FILE = "./static/players.json"
WHITELIST_JSON_FILE = "./static/whitelist.json"


def get_player_uuid(player):
    with open(WHITELIST_JSON_FILE, "r") as readFile:
        whitelist_json = json.load(readFile)

    for playerJson in whitelist_json:
        if playerJson["name"] == player:
            return playerJson["uuid"]
