import os
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
from dotenv import load_dotenv

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="Ты повар"
        )
    ],
    temperature=0.7,
)

with GigaChat(credentials=my_credentials) as giga:
    while True:
        user_input = input("User: ")
        if user_input == "пока":
            break
        payload.messages.append(Messages(role=MessagesRole.USER, content=user_input))
        response = giga.chat(payload)
        payload.messages.append(response.choices[0].message)
        print("Bot: ", response.choices[0].message.content)
