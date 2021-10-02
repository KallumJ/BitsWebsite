from player_rpc_client import PlayerRPCClient
import json

client = PlayerRPCClient()


def get_uuid_from_username(username):
    payload = {
        "query": "query($name: String!) { player(name: $name) { uuid }}",
        "variables": {"name": username}
    }
    response = json.loads(client.call(json.dumps(payload)))
    uuid = response["player"]["uuid"]

    return uuid


def get_effective_name_from_uuid(uuid):
    payload = {
        "query": "query($uuid: ID!) { player(uuid: $uuid) { username, nickname }}",
        "variables": {"uuid": uuid}
    }

    response = json.loads(client.call(json.dumps(payload)))

    playerObj = response["player"]
    if "nickname" in playerObj:
        return playerObj["nickname"]
    else:
        return playerObj["username"]


def get_list_of_vip_uuids():
    payload = {
        "query": "query { players { uuid, vip }}",
        "variables": {}
    }

    response = json.loads(client.call(json.dumps(payload)))

    uuids = []
    for player in response["players"]:
        if player["vip"]:
            uuids.append(player["uuid"])

    return uuids
