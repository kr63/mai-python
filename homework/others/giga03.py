import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_gigachat.chat_models import GigaChat
from pydantic import BaseModel, Field

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)


class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")


parser = JsonOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Ответь на запрос пользователя\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

joke_query = "Напиши мне шутку"
result = chain.invoke({"query": joke_query})
print(result)
