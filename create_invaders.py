"""This file was used to create the invader avatars from icons downloaded from google"""

from PIL import Image
import PIL.ImageOps

ICONS = ["invader_1.png", "invader_2.png", "invader_3.png", "spaceship.png"]

def add_filename_suffix(orig_file, suffix):
    old_name = orig_file[:len(orig_file)-orig_file[::-1].find(".")-1]
    file_ext = orig_file[len(old_name):]
    new_name = old_name + suffix
    return new_name + file_ext


def create_invaders(icon_list):
    """Function used to create invader turtle images from downloaded images"""
    for icon in icon_list:
        icon_img = PIL.Image.open(icon)
        icon_img_small = icon_img.resize((50, 50), PIL.Image.ANTIALIAS)
        small_filename = add_filename_suffix(icon, "_small")
        # icon_img_small.save("invader_1_small_v3.png")
        # image = Image.open("invader_1_small_v3.png")
        if icon_img_small.mode == 'RGBA':
            r,g,b,a = icon_img_small.split()
            rgb_image = PIL.Image.merge('RGB', (r,g,b))

            inverted_image = PIL.ImageOps.invert(rgb_image)

            r2,g2,b2 = inverted_image.split()

            final_transparent_image = PIL.Image.merge('RGBA', (r2,g2,b2,a))

            final_transparent_image.save(small_filename)

        else:
            inverted_image = PIL.ImageOps.invert(icon_img_small)
            inverted_image.save(small_filename)

# create_invaders(ICONS)