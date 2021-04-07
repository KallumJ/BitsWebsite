from flask import render_template, redirect, url_for, Blueprint, request

from donors import get_donor_player_list
from images import get_home_slideshow_images, get_bitsplus_slideshow_images
from products import get_all_products
from profiles import get_all_player_profiles
from serverstatus import get_bitsplus_status, get_vanilla_status
from events_database_connector import Database

routes = Blueprint("routes", __name__, template_folder="templates")


@routes.route("/")
def home():
    return render_template("home.html", vStatus=get_vanilla_status(), bStatus=get_bitsplus_status(),
                           home_slides_src=get_home_slideshow_images())


@routes.route("/store/")
def store():
    return render_template("store.html", products=get_all_products())


@routes.route("/donate/")
def donate():
    return render_template("donate.html", donorList=get_donor_player_list())


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
    return redirect(url_for("rules_whitelist"))


@routes.route("/rules/")
def rules():
    return redirect(url_for("rules_whitelist"))


@routes.route("/plugin-info/")
def plugin_info():
    return render_template("plugin-info.html")


@routes.route("/events/")
def events():
    return render_template("events.html", events_list=Database().get_agenda())