import os
import textwrap

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
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

# Invoking the synopsis chain with the initial input
synopsis = synopsis_chain.invoke({"title": title})

# Set the desired width
wrap_width = 80

# Splitting the synopsis into paragraphs
paragraphs = synopsis.split('\n\n')

# Formatting each paragraph
formatted_synopsis = '\n\n'.join([textwrap.fill(paragraph, width=wrap_width) for paragraph in paragraphs])

# Print the formatted synopsis
print('Synopsis')
print('----------------------------------')
print(formatted_synopsis)

# Invoking the review chain with the initial input
review = review_chain.invoke({"synopsis": synopsis})

# Set the desired width
wrap_width = 80

# Splitting the review into paragraphs
paragraphs = review.split('\n\n')

# Formatting each paragraph
formatted_review = '\n\n'.join([textwrap.fill(paragraph, width=wrap_width) for paragraph in paragraphs])

# Print the formatted review
print('Review')
print('----------------------------------')
print(formatted_review)

# Invoking the summary chain with the initial input
summary = summary_chain.invoke({"review": review})

# Set the desired width
wrap_width = 80

# Wrap the text
wrapped_summary = textwrap.fill(summary, width=wrap_width)

# Print the wrapped text
print('Short Summary')
print('----------------------------------')
print(wrapped_summary)
