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

    except ConnectionError as err:
        print("{} API did not respond. {}".format(server, err))
        return server_data

    return server_data


class Player:
    name = ""
    uuid = ""
    img_src = ""
