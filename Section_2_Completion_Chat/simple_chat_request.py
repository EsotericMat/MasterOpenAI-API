from completion_chat import chat
""" For the first and simple example, Let's create assistant that suggest a songs for user mood: """
chat(
    system_content='You are assistance that choose the best song for user mood',
    user_content='Im happy now!'
)