import json
import requests

playersJsonFile = "./static/players.json"
whitelistJsonFile = "./static/whitelist.json"

def getDonorUUIDs():
    donorList = []

    with open(playersJsonFile, "r") as readFile:
        playerJson = json.load(readFile)

    for player in playerJson["players"]:
        donor = player.get("donor")

        if donor:
            donorList.append(player["UUID"])

    return donorList


def getDonorPlayerList():
    donors = []

    with open(whitelistJsonFile, "r")  as readFile:
        whitelistJson = json.load(readFile)

    for uuid in getDonorUUIDs():
    
        # Check whitelist for matching player, if found, add their name and head to the donors list
        for playerJson in whitelistJson:
            if playerJson["uuid"] == uuid:
                playerDict = {
                    "username": "",
                    "headImage": ""
                }

                playerDict["username"] = playerJson["name"]
                playerDict["headImage"] = "https://visage.surgeplay.com/head/" + uuid
                donors.append(playerDict)
        

    return donors