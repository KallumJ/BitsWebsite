from discord_markdown.discord_markdown import convert_to_html
import os
from file_utils import get_player_uuid

PROFILES_DIR = "./static/assets/profiles/"


def get_all_player_profiles():
    player_profiles_list = []

    for file in os.listdir(PROFILES_DIR):
        profile_file = open(PROFILES_DIR + file, "r")

        player_profile = PlayerProfile()

        # Make the name of the player, the file name
        player_profile.name = os.path.splitext(os.path.basename(profile_file.name))[0]

        # Convert the file content to html
        player_profile.html_profile = convert_to_html(profile_file.read())

        player_profile.player_img = "https://visage.surgeplay.com/full/832/" + get_player_uuid(player_profile.name)

        player_profiles_list.append(player_profile)

    return player_profiles_list


class PlayerProfile:
    name = ""
    html_profile = ""
    player_img = ""
