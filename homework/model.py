from typing import List

from pydantic import BaseModel, Field


class Ingredient(BaseModel):
    name: str = Field(description="Название продукта")
    amount: str = Field(description="Количество продукта")


class Recipe(BaseModel):
    title: str = Field(description="Название блюда")
    description: str = Field(description="Описание блюда")
    instructions: str = Field(description="Рецепт блюда")
    ingredients: List[Ingredient] = Field(description="Список продуктов")


class Ingredients(BaseModel):
    ingredients: List[Ingredient] = Field(description="Список продуктов")
