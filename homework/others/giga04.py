import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_gigachat.chat_models import GigaChat

from homework.model import Recipe

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

parser = JsonOutputParser(pydantic_object=Recipe)

prompt = PromptTemplate(
    template="Ты повар. Напиши рецепт блюда.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

meal = "Борщ"
result = chain.invoke({"query": meal})
print(result)
