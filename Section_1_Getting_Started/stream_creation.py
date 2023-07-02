import openai

from creation import create
"""
In simple create command, the data will be collected, and printed out in the same time. 
The stream option, create a stream response (Python generator), allow us to print any piece of data that we get, and it 
will allow the model to comment faster, print out phrase after phrase.
"""
for stream in openai.Completion.create(
        model='text-davinci-003',
        prompt='Write me a 5 sentences about French culture',
        max_tokens = 150,
        stream=True):
    print(stream['choices'][0]['text'], end="", flush=True)