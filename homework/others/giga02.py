import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_gigachat.chat_models import GigaChat

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

system_template = "Ты повар. Напиши рецепт блюда {meal}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template)]
)

parser = StrOutputParser()
chain = prompt_template | model | parser
result = chain.invoke({"meal": 'борщ'})
print(result)
print('ready!')
