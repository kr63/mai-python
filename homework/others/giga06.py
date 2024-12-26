import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_gigachat.chat_models import GigaChat

from homework.model import Recipe

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

model = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

prompt_initial = PromptTemplate.from_template("Ты повар. Напиши рецепт блюда {meal}")
prompt_recipe = PromptTemplate(
    template="Ты программист. Напиши рецепт блюда.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": JsonOutputParser(pydantic_object=Recipe).get_format_instructions()},
)





meal = 'борщ'
chain_initial = prompt_initial | model | StrOutputParser()
chain_recipe = prompt_recipe | model | JsonOutputParser(pydantic_object=Recipe)

chain = (
        {"query": chain_initial}
        | RunnablePassthrough.assign(review=chain_recipe)
        # | RunnablePassthrough.assign(summary=summary_chain)
)

result = chain.invoke({"meal": meal})
print(result['query'])
print(result['review'])
