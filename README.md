# API_Yatube

## Описание

API_Yatube - это REST API для cоциальной сети блогеров Yatube ([ссылка на github](https://github.com/FanisGi/yatube)).

Основной параметры:

- Аутентификация по JWT-токену

- Работает со всеми модулями Yatube: постами, комментариями, группами, подписчиками

- Поддерживает методы GET, POST, PUT, PATCH, DELETE

- Предоставляет данные в формате JSON

## Стек технологий

- Python 3.7
- Django 2.2
- djangorestframework
- djangorestframework-simplejwt
- djoser
- PyJWT

## Как запустить проект

- Клонировать репозиторий и перейти в него в командной строке:

`git clone git@github.com:FanisGi/api_yatube.git`

`cd api_yatube`

- Cоздать и активировать виртуальное окружение:

`python3 -m venv venv`

`source env/bin/activate`

- Установить зависимости из файла requirements.txt:

`python3 -m pip install --upgrade pip`

`pip install -r requirements.txt`

- Выполнить миграции:

`python3 manage.py migrate`

- Запустить проект:

`python3 manage.py runserver`

## Аутентификация

Выполните POST-запрос `localhost:8000/api/v1/token/` передав поля **username** и **password**.

API вернет JWT-токен в формате:

```
{
    "refresh": "ХХХХХХХХХХХ",
    "access": "ХХХХХХХХХХХХ"
}
```

Токен вернётся в поле **access**, а данные из поля **refresh** нужны для обновления токена

При отправке запроcов передавайте токен в заголовке **Authorization: Bearer <токен>**

## Примеры запросов API:

После запуска проекта переходите на 

```
http://127.0.0.1:8000/redoc/
```

Там будут все примеры запросов и даже больше.
