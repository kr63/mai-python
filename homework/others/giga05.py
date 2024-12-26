import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langchain_gigachat.chat_models import GigaChat

from homework.model import Ingredients

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

parser = JsonOutputParser(pydantic_object=Ingredients)
parser = StrOutputParser()

system_template = "Ты повар. Напиши рецепт блюда {meal}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template)]
)

chain = prompt_template | model | parser
result = chain.invoke({"meal": 'борщ'})
print(result)
print('ready!')
