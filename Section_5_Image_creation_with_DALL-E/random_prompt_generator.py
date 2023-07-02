import openai
from dotenv import dotenv_values
config = dotenv_values('../.env')
# Configure Open AI Key:
openai.api_key = config['API_KEY']

if __name__ == '__main__':
    p = openai.Completion.create(
        model='text-davinci-003',
        prompt="Create a nice detailed high quality random prompt for DALL-E, about any subject you can think about",
        max_tokens = 125
        )['choices'][0]['text']
    print(p)


