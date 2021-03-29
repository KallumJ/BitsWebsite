import json

from file_utils import get_whitelist_file, get_players_file


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

    whitelist_json = get_whitelist_file()

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
