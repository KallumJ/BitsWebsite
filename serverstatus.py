import requests
from requests.exceptions import ConnectionError


def get_vanilla_status():
    return get_server_status("https://bits.team/api/players?server=vanilla")


def get_bitsplus_status():
    return get_server_status("https://localhost")


def get_server_status(server):
    server_data = {
        "online": False,
        "player_count": 0,
        "player_img_srcs": []
    }

    try:
        response_json = requests.get(server).json()

        server_data["online"] = True

        for player in response_json:

            server_data["player_count"] += 1

            server_data["player_img_srcs"].append("https://visage.surgeplay.com/head/" + player["uuid"])
    except ConnectionError as err:
        print("{} API did not respond. {}".format(server, err))
        return server_data

    return server_data

