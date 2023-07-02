from creation import create
"""
In this section we can see how to feed the algorithm with a structured prompt (e.g - conversation) and get back 
an optional responses. 
To keep the conversation, we can run one line at a time, using `stop=` argument, and expand the prompt every run.
"""

prompt = """
User: Hi! I need help with my new laptop
Technician: Ill glad to help, what laptop do you have?
User: I have a MacBook Air M1
Technician: Great, and what is your problem?
User: I tried to install Python, But I can't! Can you explain to me what shoul'd I do?
Technician: 
"""

# Every time that the model will go up to one of the items in the list, he will stop, and this will prove one line at a
stop = ['User: ', 'Technician:']

create(prompt=prompt, max_tokens=150)