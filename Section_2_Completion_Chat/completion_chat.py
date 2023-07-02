import openai
from dotenv import dotenv_values

config = dotenv_values('../.env')

# Configure Open AI Key:
openai.api_key = config['API_KEY']


def chat(system_content=None, user_content=None, examples=[]):
    """This time we use ChatCompletion API command"""
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        # Inside this parameter, we are giving examples for the chat to learn from {role: xyz ,content: wvu} etc.
        messages=[
            {'role': 'system', 'content': system_content},
            {'role': 'user', 'content': user_content},
        ] + examples,
        max_tokens=220
    )
    results_print = response['choices'][0]['message']
    print(f"{results_print['role']}: {results_print['content']}")


