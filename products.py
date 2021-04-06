from file_utils import get_products_file

def get_all_products():
    product_file = get_products_file()

    products_list = []
    for product in product_file:
        product_obj = Product()

        product_obj.name = product["name"]
        product_obj.image = product["image"]
        product_obj.url = product["url"]

        products_list.append(product_obj)

    return products_list


class Product:
    name = ""
    image = ""
    url = ""
