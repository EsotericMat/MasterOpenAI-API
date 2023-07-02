import openai
from dotenv import dotenv_values

config = dotenv_values('../.env')

# Configure Open AI Key:
openai.api_key = config['API_KEY']


class CodeAssitance:

    def __init__(self):
        self.key = openai.api_key
        self.system_content_opening = 'You are a developers assistance, who help them with code writing and exploration.'

    def basic_response(self, system_content, user_content):
        report = []
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[
                {'role': 'system', 'content': system_content},
                {'role': 'user', 'content': user_content}
            ],
            stream=True
        )
        for res in response:
            cont = res['choices'][0]['delta'].get('content')
            if not cont is None:
                #     pass
                # elif cont == ".":
                #     print(cont + '\n')
                # else:
                print(cont, end="")

    def explain(self, code_as_a_text):
        self.basic_response(
            system_content=f'{self.system_content_opening} You get a code snippet, and help the developer to understand'
                           f'it with a simple language and short example if possible.',
            user_content=code_as_a_text
        )

    def translate(self, lang_in, lang_out, code_as_a_text):
        self.basic_response(
            system_content=f'{self.system_content_opening},You get a code snippet in {lang_in} and translate it to'
                           f'{lang_out}',
            user_content=code_as_a_text
        )

    def find_bugs(self, code_as_a_text):
        self.basic_response(
            system_content=f'{self.system_content_opening},You get a code snippet with a bug, and you need to find '
                           f'out what is the bug,where he located and how to fix it',
            user_content=code_as_a_text
        )

    def write_code(self, request, lang):
        self.basic_response(
            system_content=f'{self.system_content_opening},You got a request, containing characteristics for the '
                           f'needed code snippet, and write it from scratch in {lang}.'
                           f'Please add a short explanation about the components, and how to use it.',
            user_content=request
        )
