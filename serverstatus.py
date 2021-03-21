import requests
import json

def getVanillaStatus():
    return getServerStatus("play.bits.team")


def getBitsPlusStatus():
    return getServerStatus("plus.bits.team")


def getServerStatus(server):
    serverData = {
        "online": False,
        "playerCount": 0
    }

    #responseJson = requests.get(server).json()

    #serverData["online"] = responseJson["online"]
    
    #if serverData["online"] == True:
    #    serverData["playerCount"] = responseJson["players"]["online"]

    return serverData

