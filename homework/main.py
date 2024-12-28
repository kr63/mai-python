import argparse

from markdown_generator import generate_markdown
from recipe_generator import generate_recipe
from yandex_eda import search_yandex_eda


def get_yandex_id(ingredients):
    # key -> name; value -> public_id
    result = dict()
    for item in ingredients:
        response = search_yandex_eda(item['name'])
        response = response['blocks']
        response = response[0]
        response = response['payload']
        response = response['products'][0]
        result[item['name']] = response['public_id']
    return result

def run(meal: str, filename: str):
    result = generate_recipe(meal)
    public_ids = get_yandex_id(result['ingredients'])
    return generate_markdown(result, public_ids, filename)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Генератор рецептов')
    parser.add_argument('-m', '--meal', type=str,
                        help='Название блюда', default='борщ')
    parser.add_argument('-o', '--out', type=str,
                        help='Итоговый файл', default='recipe.md')
    args = parser.parse_args()
    md = run(args.meal, args.out)
    md.create_md_file()
