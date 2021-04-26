from json.decoder import JSONDecodeError

import requests
from requests.exceptions import ConnectionError

from config import vanillaLocalServerAPI, vanillaRemoteServerAPI, creativeLocalServerAPI, creativeRemoteServerAPI
from remote_server_utils import check_on_hogwarts


def get_vanilla_status():
    if check_on_hogwarts():
        return get_server_status(vanillaLocalServerAPI)
    else:
        return get_server_status(vanillaRemoteServerAPI)


def get_creative_status():
    if check_on_hogwarts():
        return get_server_status(creativeLocalServerAPI)
    else:
        return get_server_status(creativeRemoteServerAPI)


def get_server_status(server):
    server_data = {
        "online": False,
        "player_count": 0,
        "player_list": []
    }

    try:
        response_json = requests.get(server).json()

        server_data["online"] = True

        for player in response_json:
            player_obj = Player()
            player_obj.name = player["name"]
            player_obj.uuid = player["uuid"]
            player_obj.img_src = "https://visage.surgeplay.com/head/" + player["uuid"]

            server_data["player_list"].append(player_obj)

            server_data["player_count"] += 1

    except (ConnectionError, JSONDecodeError) as err:
        print("{} API did not respond. {}".format(server, err))
        return server_data

    return server_data


class Player:
    name = ""
    uuid = ""
    img_src = ""
