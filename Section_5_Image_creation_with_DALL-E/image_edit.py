import openai
from dotenv import dotenv_values
from save_images import get_and_save_image
config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']

res = openai.Image.create_edit(
    image=open('images/random_girl.png', 'rb'),
    mask=open('images/random_girl_masked.png', 'rb'),
    prompt="Green field and a castle in the view behind"
)
url = res['data'][0]['url']
get_and_save_image(url, 'editing_a')