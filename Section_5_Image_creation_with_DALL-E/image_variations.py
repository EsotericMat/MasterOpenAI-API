import openai
from dotenv import dotenv_values
from save_images import get_and_save_image
config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']


res = openai.Image.create_variation(
    image=open('images/random_girl.png', 'rb')
    , n=1
)

url = res['data'][0]['url']

get_and_save_image(url, 'random_girl_variant_c')


