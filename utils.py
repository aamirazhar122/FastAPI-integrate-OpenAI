from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
from openai.types.chat.chat_completion import ChatCompletion

_ : bool = load_dotenv(find_dotenv())
client : OpenAI = OpenAI()

def user_answer(prompt : str)->str :
    response : ChatCompletion=client.chat.completions.create(
        model = 'gpt-3.5-turbo-1106',
        messages=[
            {
                'role' : 'system', 'content' : 'you are a assistant chatbot for answering of asked questions',
                'role'  : 'user', 'content' : f'{prompt}',
            }
        ]
    )
    reply = response.choices[0].message.content
    return reply

