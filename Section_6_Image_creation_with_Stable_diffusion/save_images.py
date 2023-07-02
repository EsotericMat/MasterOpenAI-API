import os
import string
import requests
import random


def random_string_img_name(n):
    """Generate random string file name for images"""
    if n < 5:
        raise ValueError("Must be at least 5 characters long")

    chars  = string.digits + string.ascii_lowercase
    return ''.join(random.choices(chars, k=n))


def make_images_dir():
    """Make sure the directory for the generated images is existed"""
    img_dir = 'images'
    img_path = os.path.join(os.curdir, img_dir)

    if not os.path.isdir(img_path):
        os.mkdir(img_path)

    return img_path


def get_and_save_image(img_content, name=None):
    """Create file, read URL and write the content into the file"""

    img_base = make_images_dir()

    if name:
        img_name = f'SD_{name}.png'
    else:
        img_name=f'SD_{random_string_img_name(8)}.png'

    img_directory = os.path.join(img_base, img_name)

    with open (img_directory, 'wb') as img:
        img.write(img_content)
        img.close()

    return f'{img_directory} Is created'
