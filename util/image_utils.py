import os


def get_home_slideshow_images():
    return get_image_srcs("./static/assets/images/homeslideshow/")


def get_bitsplus_slideshow_images():
    return get_image_srcs("./static/assets/images/bitsplusslideshow")


def get_image_srcs(directory_path):
    img_src = "../." + directory_path + "/{}"

    file_list = []

    for file in os.listdir(directory_path):
        pos = get_image_pos_in_list(file)
        src = img_src.format(file)
        file_list.insert(pos, src)

    return file_list

def get_image_pos_in_list(file):
    try:
        return int(file.split(".")[0])
    except ValueError:
        return -1
    