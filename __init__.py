from flask import Flask, render_template, send_from_directory
import os
from serverstatus import getBitsPlusStatus, getVanillaStatus

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", vStatus = getVanillaStatus(), bStatus = getBitsPlusStatus())


@app.route("/store")
def store():
    return render_template("store.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


@app.route("/downloads")
def downloads():
    return render_template("downloads.html")


@app.route("/bitsplus")
def bitsplus():
    return render_template("bitsplus.html")

    
if __name__ == "__main__":
    app.run(debug=True)
