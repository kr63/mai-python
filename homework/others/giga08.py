import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_gigachat.chat_models import GigaChat

from homework.model import Ingredients, Recipe

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)


def call_llm(_parser, _prompt, _request):
    _chain = _prompt | model | _parser
    return _chain.invoke(_request)


meal = "Борщ"
request = {"meal": meal}

parser = JsonOutputParser(pydantic_object=Recipe)
prompt = PromptTemplate(
    template="Ты повар. Как приготовить блюдо.\n{format_instructions}\n{meal}\n",
    input_variables=["meal"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
result1 = call_llm(parser, prompt, request)
print(result1)
print('-' * 80)

parser = JsonOutputParser(pydantic_object=Ingredients)
system_template = "Сгенерируй ингредиенты для {meal}. " + \
                  "Результат верни в формате JSON-массива без каких-либо пояснений. " + \
                  "например, [{{ \"name\": \"название объекта\", \"amount\": \"количество\" }}]."
prompt = ChatPromptTemplate.from_messages([("system", system_template)])
result2 = call_llm(parser, prompt, request)
print(result2)
print('ready!')
