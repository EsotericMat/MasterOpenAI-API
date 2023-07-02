from completion_chat import chat
"""
You can refine the assistance answer by giving him example. This can be usefull if you want him to talk straight forward 
without any greetings / feeling etc.
We will keep using the same assistance, that choosing songs by user mood, But now I want only 1 song, and only the name.
"""
chat(
    system_content='You are assistance that choose the best song for user mood',
    user_content='Im Sad...',
    examples= [
        {'role':'assistant', 'content':'"Hurt" by Johnny Cash'}, #
        {'role':'user', 'content':'I am Sad'}
    ]
)