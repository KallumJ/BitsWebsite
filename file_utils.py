import json

PLAYERS_JSON_FILE = "./static/players.json"
WHITELIST_JSON_FILE = "./static/whitelist.json"
PRODUCTS_JSON_FILE = "./static/products.json"


def get_player_uuid(player):
    with open(WHITELIST_JSON_FILE, "r") as read_file:
        whitelist_json = json.load(read_file)

    for playerJson in whitelist_json:
        if playerJson["name"] == player:
            read_file.close()
            return playerJson["uuid"]


def get_player_name_from_uuid(uuid):
    with open(WHITELIST_JSON_FILE, "r") as read_file:
        whitelist_json = json.load(read_file)

    for playerJson in whitelist_json:
        if playerJson["uuid"] == uuid:
            read_file.close()
            return playerJson["name"]


def get_whitelist_file():
    with open(WHITELIST_JSON_FILE, "r") as read_file:
        whitelist_json = json.load(read_file)

    read_file.close()
    return whitelist_json


def get_players_file():
    with open(PLAYERS_JSON_FILE, "r") as read_file:
        player_json = json.load(read_file)

    read_file.close()
    return player_json


def get_products_file():
    with open(PRODUCTS_JSON_FILE, "r") as read_file:
        products_json = json.load(read_file)

    read_file.close()
    return products_json
