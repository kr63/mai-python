from mdutils import MdUtils

BASE_LINK = 'https://eda.yandex.ru/retail/perekrestok?item='


def generate_markdown(_recipe, _public_ids, filename='recipe.md'):
    md = MdUtils(file_name=filename, title=_recipe['title'])
    md.new_header(level=1, title='Описание')
    md.new_paragraph(_recipe['description'])
    md.new_header(level=1, title='Ингредиенты')
    links = list()
    for item in _recipe['ingredients']:
        name = item['name']
        link = md.new_inline_link(link=BASE_LINK + _public_ids[name], text=name)
        links.append('{} {}'.format(link, item['amount']))
    md.new_list(links, marked_with='1')
    md.new_header(level=1, title='Готовка')
    md.new_list([item for item in _recipe['instructions']], marked_with='1')
    return md


if __name__ == '__main__':
    public_ids = {'говядина на кости': '8b4e43d3-540c-4717-b754-3a1c86b49d6d',
                  'свекла': '5095806e-2670-463e-a558-c22c7a906d30'}
    recipe = \
        {
            "title": "Классический борщ",
            "description": "Традиционный русский суп с насыщенным вкусом.",
            "ingredients": [
                {"name": "говядина на кости", "amount": "500 г"},
                {"name": "свекла", "amount": "2 шт."},
            ],
            "instructions": [
                "Поставь говядину вариться на медленном огне в большой кастрюле с водой. Варить около 1,5 часов до готовности мяса.",
                "Свеклу очисти и натри на крупной терке. Обжарь свеклу на растительном масле с добавлением уксуса и сахара, затем добавь томатную пасту и туши еще 10 минут.",
            ]
        }
    md = generate_markdown(recipe, public_ids)
    print(md.file_data_text)
