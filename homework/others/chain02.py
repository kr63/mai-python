import os
import textwrap

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_gigachat import GigaChat

load_dotenv()
my_credentials = os.getenv('MY_CREDENTIALS')

llm = GigaChat(
    credentials=my_credentials,
    scope="GIGACHAT_API_PERS",
    model="GigaChat"
)

synopsis_prompt = PromptTemplate.from_template(
    """Ты драматург. Напиши краткое содержание пьесы.
    Название: {title}
    """
)

review_prompt = PromptTemplate.from_template(
    """Ты литературный критик. Дано краткое содержание пьесы, Твоя задача написать обзор.
    Краткое содержаение: {synopsis}
    """
)

summary_prompt = PromptTemplate.from_template(
    """Ты журналист, Напиши обзор на пьесу в двух предложениях.
    Обзор: {review}
    """
)

# Setting the initial input for the chain
title = "Сказка о рыбаке и рыбке"

synopsis_chain = synopsis_prompt | llm | StrOutputParser()
review_chain = review_prompt | llm | StrOutputParser()
summary_chain = summary_prompt | llm | StrOutputParser()

chain = (
    {"synopsis": synopsis_chain}
    | RunnablePassthrough.assign(review=review_chain)
    | RunnablePassthrough.assign(summary=summary_chain)
)

result = chain.invoke({"title": title})

# Wrapping the output text for readability
wrap_width = 80  # Defines the maximum width of each line in the output
print("Output:")
print("-------------------------------------------------------------------")
for key, value in result.items():
    print(f"{key.capitalize()}:")
    paragraphs = value.split('\n\n')
    for paragraph in paragraphs:
        wrapped_paragraph = textwrap.fill(paragraph, width=wrap_width)
        print(wrapped_paragraph)
        print()