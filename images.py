import os


def get_home_slideshow_images():
    return get_image_srcs("./static/assets/images/homeslideshow")


def get_bitsplus_slideshow_images():
    return get_image_srcs("./static/assets/images/bitsplusslideshow")


def get_image_srcs(directory_path):
    img_src = "../." + directory_path + "/{}"

    file_list = []

    for file in os.listdir(directory_path):
        file_list.append(img_src.format(file))

    return file_list

