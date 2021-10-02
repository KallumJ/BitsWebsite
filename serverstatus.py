from remote_server_utils import check_on_hogwarts
from server_rpc_client import ServerRPCClient
import json

client = ServerRPCClient()


def get_ravenclaw_status():
    if check_on_hogwarts():
        return get_server_status("ravenclaw")
    else:
        return get_server_status("localhost")


def get_hufflepuff_status():
    if check_on_hogwarts():
        return get_server_status("hufflepuff")
    else:
        return get_server_status("localhost")


def get_server_status(server):
    server_data = {
        "online": False,
        "player_count": 0,
        "player_list": [],
        "version": ""
    }

    try:
        payload = {
            "query": "query($hostname: String!) { status(hostname: $hostname) { version { name }, players { online, sample { name, id } } } }",
            "variables": {"hostname": server}
        }

        response = json.loads(client.call(json.dumps(payload)))

        info = response["status"]
        if "version" in info:
            server_data["online"] = True
            server_data["version"] = info["version"]["name"]
            server_data["player_count"] = info["players"]["online"]

            for player in info["players"]["sample"]:
                player_obj = Player()
                player_obj.name = player["name"]
                player_obj.uuid = player["id"]
                player_obj.img_src = "https://visage.surgeplay.com/head/" + player["id"]

                server_data["player_list"].append(player_obj)

    except Exception as err:
        print("{} API did not respond. {}".format(server, err))
        return server_data

    return server_data


class Player:
    name = ""
    uuid = ""
    img_src = ""

