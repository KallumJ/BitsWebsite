from flask import Flask, render_template
from serverstatus import get_bitsplus_status, get_vanilla_status
from donors import get_donor_player_list
from images import get_home_slideshow_images, get_bitsplus_slideshow_images

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", vStatus=get_vanilla_status(), bStatus=get_bitsplus_status(),
                           home_slides_src=get_home_slideshow_images())


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/store")
def store():
    return render_template("store.html")


@app.route("/donate")
def donate():
    return render_template("donate.html", donorList=get_donor_player_list())


@app.route("/downloads")
def downloads():
    return render_template("downloads.html")


@app.route("/bitsplus")
def bitsplus():
    return render_template("bitsplus.html",
                           bitsplus_slides_src=get_bitsplus_slideshow_images())


if __name__ == "__main__":
    app.run(debug=True)
