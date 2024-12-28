import argparse

from gigachat import generate_recipe

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Генератор рецептов')
    parser.add_argument('-m', '--meal', type=str,
                        help='Название блюда', default='борщ')
    args = parser.parse_args()
    print(args.meal)

    result = generate_recipe(args.meal)

    print(f'title: {result['title']}')
    print(f'title: {result['description']}')
    for item in result['instructions']:
        print(item)
    for item in result['ingredients']:
        print(item['name'], item['amount'])

