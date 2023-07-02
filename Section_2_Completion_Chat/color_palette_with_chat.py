from completion_chat import chat

"""
Now let's try to mimic our project from section 1, that required long and complicated prompt (Questions, Answers).
This time we will do it with the Chat (10x cheaper!)
"""

chat(
    system_content='You are assistant that create a color palettes, structured as a Python list, from user text',
    user_content='4 colors Google brand',
    examples=[
        {"role": "assistant", "content": "['#4285F4', '#FBBC05', '#34A853', '#EA4335']"},
        {"role": "user", "content": "LA Lakers Brand 3 colors"}
    ]
)