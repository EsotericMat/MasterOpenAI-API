from creation import create

"""
Echo p[tion allow us to include our prompt in the output, It's nice when you have a Q n A creation or something
like that.
OpenAI will not extra charge on Echo commands.
"""

prompt = 'In 1 words, what is the most comfort food you ever tasted?'
create(prompt, echo=True)
