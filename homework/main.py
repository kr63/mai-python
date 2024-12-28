import argparse

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

def run(meal: str):
    result = generate_recipe(meal)
    public_ids = get_yandex_id(result['ingredients'])
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Генератор рецептов')
    parser.add_argument('-m', '--meal', type=str,
                        help='Название блюда', default='борщ')
    args = parser.parse_args()
    # print(args.meal)
    run(args.meal)

    # result = generate_recipe(args.meal)
    #
    # print(f'title: {result['title']}')
    # print(f'title: {result['description']}')
    # for item in result['instructions']:
    #     print(item)
    # for item in result['ingredients']:
    #     print(item['name'], item['amount'])

'https://eda.yandex.ru/retail/perekrestok?item=[public_id].'
