import numpy
import openai
import argparse
from dotenv import dotenv_values
config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']

parser = argparse.ArgumentParser()
parser.add_argument('-txt', type=str, help='Text to embedding')
args = parser.parse_args()


def embed(text):
    res = openai.Embedding.create(
        input=text,
        model='text-embedding-ada-002'
    )
    return res['data'][0]['embedding']


if __name__ == '__main__':
    vec = embed(args.txt)
    print(vec[:10])
