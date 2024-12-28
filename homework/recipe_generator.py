import os

from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_gigachat.chat_models import GigaChat

from model import Recipe

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

template = """Ты повар. Напиши ингредиенты для приготовления блюда: {meal}. 
            Результат верни в формате JSON без каких-либо пояснений. 
            например, {{ \"title\": \"название блюда\", \"description\": \"описание блюда\",
            \"instructions\": [\"подробный рецепт блюда по пунктам\"], 
            \"ingredients\": [{{ \"name\": \"название ингредиента\", \"amount\": \"количество\"] }}] }}.
            """

def generate_recipe(meal: str):
    prompt = ChatPromptTemplate.from_messages(
        [("system", template)]
    )

    parser = JsonOutputParser(pydantic_object=Recipe)
    chain = prompt | model | parser
    return chain.invoke({"meal": meal})
