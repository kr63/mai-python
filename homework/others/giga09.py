import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_gigachat.chat_models import GigaChat

from homework.model import Ingredients

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

system_template = "Ингредиенты для приготовления блюда: {meal}. " + \
                  "Результат верни в формате JSON-массива без каких-либо пояснений. " + \
                  "например, [{{ \"name\": \"название объекта\", \"amount\": \"количество\" }}]."
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template)]
)

parser = JsonOutputParser(pydantic_object=Ingredients)
chain = prompt_template | model | parser
result = chain.invoke({"meal": 'борщ'})
print(result)
print('ready!')
