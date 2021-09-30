import json

PRODUCTS_JSON_FILE = "./static/products.json"

def get_products_file():
    with open(PRODUCTS_JSON_FILE, "r") as read_file:
        products_json = json.load(read_file)

    read_file.close()
    return products_json
