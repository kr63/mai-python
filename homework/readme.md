## Генерация рецептов с помощью gigachat

### Настройка
В корень проекта добавить файл .env с содержимым:

```shell
MY_CREDENTIALS="ключ авторизации для доступа к api gigachat"
BASE_URL="https://eda.yandex.ru"
```

BASE_URL - url для поиска в яндекс еде. Можно запустить mock сервер, чтобы не пользоваться реальным api яндекса:
```shell
BASE_URL=http://localhost:8080
java -jar ./wiremock/wiremock-standalone-3.10.0.jar
```
Тогда поиск поиск будет осуществляться по адресу:
```shell
https://localhost:8080/api/v1/menu/search
```

Примеры запросов см. wiremock/request.http

### Запуск проекта
```shell
python ./main.py -m 'луковый суп' -o 'рецепт.md'
```

Рецепт будет записан в файле 'рецепт.md'

### Help
```shell
python ./main.py -h
```