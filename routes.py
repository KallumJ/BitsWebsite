from flask import render_template, redirect, url_for, Blueprint, send_file

from util.image_utils import get_home_slideshow_images, get_bitsplus_slideshow_images
from util.product_utils import get_all_products
from util.profile_utils import get_all_player_profiles
from api.server_status_api import get_hufflepuff_status, get_ravenclaw_status
import util.file_utils as file_utils

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

@routes.route("/discord/")
def discord():
    return redirect('https://discord.com/invite/Arfcnku')

@routes.route("/download/resourcepack")
def download_resource_pack():
    file_utils.download_resource_pack()

    return send_file(file_utils.RESOURCE_PACK_ZIP, as_attachment=True)

@routes.route("/map")
def map():
    return redirect("https://map.bits.team")

@routes.route("/tutorials")
def tutorials():
    return render_template("tutorials.html")

@routes.route("/clips")
def clips():
    return redirect("https://clips.bits.team")
