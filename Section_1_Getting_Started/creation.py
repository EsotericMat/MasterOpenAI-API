import openai
from dotenv import dotenv_values

config = dotenv_values('../.env')

# Configure Open AI Key:
openai.api_key = config['API_KEY']


def create(prompt,return_full_response=False, max_tokens=100, n=1, echo=False, stream=False):
    response = openai.Completion.create(
        model='text-davinci-003',
        prompt=prompt,
        max_tokens=max_tokens,
        n=n,
        echo=echo,
        stream=stream
    )
    if return_full_response:
        return response
        pass
    # Print the text
    # if n > 1:
    print(*[response['choices'][idx]['text'] for idx in range(n)])
    return response['choices'][0]['text']

    # else:
    #     print(response['choices'][0]['text'])

