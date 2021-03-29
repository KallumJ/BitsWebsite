from flask import Flask, render_template, redirect, url_for
from serverstatus import get_bitsplus_status, get_vanilla_status
from donors import get_donor_player_list
from images import get_home_slideshow_images, get_bitsplus_slideshow_images
from profiles import get_all_player_profiles
from products import get_all_products

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", vStatus=get_vanilla_status(), bStatus=get_bitsplus_status(),
                           home_slides_src=get_home_slideshow_images())


@app.route("/store/")
def store():
    return render_template("store.html", products=get_all_products())


@app.route("/donate/")
def donate():
    return render_template("donate.html", donorList=get_donor_player_list())


@app.route("/downloads/")
def downloads():
    return render_template("downloads.html")


@app.route("/bitsplus/")
def bitsplus():
    return render_template("bitsplus.html",
                           bitsplus_slides_src=get_bitsplus_slideshow_images())


@app.route("/player-profiles/")
def player_profiles():
    return render_template("player-profiles.html", profiles=get_all_player_profiles())


@app.route("/whitelist/")
def whitelist():
    return render_template("whitelist.html")


@app.route("/rules/")
def rules():
    return render_template("rules.html")


@app.route("/advancements-statistics/")
def advancements_statistics():
    return render_template("advancements-statistics.html")


@app.route("/events/")
def events():
    return render_template("events.html")


if __name__ == "__main__":
    app.run(debug=True)
