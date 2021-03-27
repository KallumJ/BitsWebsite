import json

PLAYERS_JSON_FILE = "./static/players.json"
WHITELIST_JSON_FILE = "./static/whitelist.json"


def get_donor_uuids():
    donor_list = []

    with open(PLAYERS_JSON_FILE, "r") as readFile:
        player_json = json.load(readFile)

    for player in player_json["players"]:
        donor = player.get("donor")

        if donor:
            donor_list.append(player["UUID"])

    return donor_list


def get_donor_player_list():
    donors = []

    with open(WHITELIST_JSON_FILE, "r") as readFile:
        whitelist_json = json.load(readFile)

        # Kall, Koenn, and our alts
        blacklist_uuids = ["b9be5135-fe8c-4a34-9e63-ffeef0fc80fb",
                           "cac04f5f-726f-4192-8290-24bdd9e7c9aa",
                           "90fd7b3f-239f-4ba4-809c-427081ebfa4e",
                           "0d594da7-6b81-463e-a0a7-d21c2e6b76f5"]

    for uuid in get_donor_uuids():

        # Check whitelist for matching player, if found,
        # add their name and head to the donors list
        for playerJson in whitelist_json:
            if playerJson["uuid"] == uuid and not blacklist_uuids.__contains__(uuid):
                player_dict = {"username": playerJson["name"], "headImage": "https://visage.surgeplay.com/head/" + uuid}

                donors.append(player_dict)

    return donors
