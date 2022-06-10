from flask import render_template, redirect, url_for, Blueprint
from flask_cors import cross_origin

from config import playerDbDefaultServer
from events_database_connector import EventsDatabase
from images import get_home_slideshow_images, get_bitsplus_slideshow_images
from player_database_connector import PlayerDatabase
from products import get_all_products
from profiles import get_all_player_profiles
from serverstatus import get_hufflepuff_status, get_ravenclaw_status

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def home():
    return render_template("home.html", vStatus=get_ravenclaw_status(), cStatus=get_hufflepuff_status(),
                           home_slides_src=get_home_slideshow_images())


@routes.route("/store/")
def store():
    return render_template("store.html", products=get_all_products())


@routes.route("/donate/")
def donate():
    return redirect("https://ko-fi.com/bitsteam")


@routes.route("/downloads/")
def downloads():
    return render_template("downloads.html")


@routes.route("/bitsplus/")
def bitsplus():
    return render_template("bitsplus.html",
                           bitsplus_slides_src=get_bitsplus_slideshow_images())


@routes.route("/player-profiles/")
def player_profiles():
    return render_template("player-profiles.html", profiles=get_all_player_profiles())


@routes.route("/rules-whitelist/")
def rules_whitelist():
    return render_template("rules-whitelist.html")


@routes.route("/whitelist/")
def whitelist():
    return redirect(url_for("routes.rules_whitelist"))


@routes.route("/rules/")
def rules():
    return redirect(url_for("routes.rules_whitelist"))


@routes.route("/apply/")
def apply():
    return redirect(url_for("routes.rules_whitelist"))


@routes.route("/plugin-info/")
def plugin_info():
    return render_template("plugin-info.html")


@routes.route("/events/")
def events():
    return render_template("events.html", events_list=EventsDatabase().get_agenda())


@routes.route("/statistics/")
def statistics():
    return render_template("statistics.html", seasons=PlayerDatabase().get_all_vanilla_seasons(),
                           top_3=PlayerDatabase().get_top_3(), default=playerDbDefaultServer)


@routes.route("/statistics_info/<season>")
@cross_origin(origin="*", headers=['Content-Type', 'Authorization'])
def statistics_get(season):
    print(PlayerDatabase().get_season_stats_json(season))

    return PlayerDatabase().get_season_stats_json(season)

@routes.route("/discord/")
def discord():
    return redirect('https://discord.com/invite/Arfcnku')

@routes.route("/tutorials")
def recording():
    return render_template("tutorials.html")