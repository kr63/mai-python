import unittest
from unittest import TestCase
from unittest.mock import patch

from homework.main import get_yandex_id
from main import run


class TestGetData(unittest.TestCase):
    @patch('main.generate_recipe')
    def test_run(self, mock):
        # given
        mock.return_value = \
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
        # when
        result = run('test')
        # then
        self.assertEqual(result, mock.return_value)

    def test_get_yandex_id(self):
        # given
        ingredients = [{"name": "говядина на кости", "amount": "500 г"},
                       {"name": "свекла", "amount": "2 шт."}, ]
        # when
        result = get_yandex_id(ingredients)
        # then
        self.assertEqual([key for key in result.keys()], [item['name'] for item in ingredients])
