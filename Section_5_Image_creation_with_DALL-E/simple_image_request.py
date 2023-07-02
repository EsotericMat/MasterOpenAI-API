import openai
from dotenv import dotenv_values
config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']


def create(text, size=256, n=1):
    n = min(n, 9)
    res = openai.Image.create(
        prompt = text,
        n=n,
        size=f'{size}x{size}'
    )
    return res['data'][0]['url']

