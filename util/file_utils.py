import json
from tempfile import TemporaryDirectory
import git
import os

PRODUCTS_JSON_FILE = "./static/products.json"
ARCHIVES_DIR = "/tmp/archives/"
RESOURCE_PACK_ZIP = ARCHIVES_DIR + "Bits Resource Pack.zip"
RESOURCE_PACK_REPO_URL = "https://hogwarts.bits.team/git/Bits/BitsResourcePack.git"

def get_products_file():
    with open(PRODUCTS_JSON_FILE, "r") as read_file:
        products_json = json.load(read_file)

    read_file.close()
    return products_json

def download_resource_pack():
    # Clone the Resource Pack Repo
    with TemporaryDirectory() as temp_dir:
        repo = git.Repo.clone_from(RESOURCE_PACK_REPO_URL, to_path=temp_dir)

        # If the archives folder doesn't exist, create it
        if not (os.path.isdir(ARCHIVES_DIR)):
            os.makedirs(ARCHIVES_DIR)

        # Zip the repo
        with open(RESOURCE_PACK_ZIP, "wb") as zip:
            repo.archive(zip, format="zip")
