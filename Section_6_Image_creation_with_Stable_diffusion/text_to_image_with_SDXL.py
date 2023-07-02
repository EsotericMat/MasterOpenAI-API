from dotenv import dotenv_values
import requests
from save_images import get_and_save_image
config = dotenv_values('../.env')
# Configure ClipboardAI Key:
key = config['CLIPDROP_KEY']


def generate(prompt):

    res = requests.post(
        'https://clipdrop-api.co/text-to-image/v1',
        files={
            'prompt': (None, prompt, 'text/plain')
        },
        headers={'x-api-key': key},
    )

    return res.content


if __name__ == '__main__':
    img = generate("""
3D art of monkey playing poker with humans sunglasses and smoke cigar
    """)

    get_and_save_image(img, 'SDXL_smoking_monkey')