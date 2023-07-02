from creation import create

"""
In this file we can see how to generate multiple options of completion to our prompt, and what is the different between
set the n value in the command, instead of just ask `give me a 5 reasons to.." in the prompt itself.
The advantage of using n=x instead of prompts instruction, is that we actually get n different data entities to work with
and not a simple long string with line breakers etc. 
We can manipulate them one by one, without writing additional code to separate the content into pieces.
"""

# Write 3 knock-knock jokes
prompt = 'Tell me a knock knock joke'
multiple_result = create(prompt, n=3)