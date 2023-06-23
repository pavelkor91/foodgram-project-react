# praktikum_new_diplom
![example workflow](https://github.com/pavelkor91/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)

# Продуктовый помощник

## IP сервера с работающим проектом - http://158.160.26.123/
Доступы от админа 
логин admin@admin.ru
пароль admin1234

## Проект «Проект Foodgram»
1. [Описание проекта](#описание-проекта)
2. [Ресурсы Foodgram](#ресурсы-foodgram)
3. [Как запустить проект](#как-запустить-проект)
4. [Примеры запросов](#пример-запроса)
5. [Стек технологий](#стек-технологий)
5. [Автор](#автор)

## Описание проекта:

Проект позволяет публиковать рецепты, добавлять в избранное и экспортировать список продуктов для покупок у выбранных рецептов. Также есть возможность подписываться на авторов интересных рецептов. 

## Ресурсы Foodgram

- Ресурс users: пользователи, подписки.
- Ресурс recipes: Рецепты, ингредиенты.
- Ресурс cart: Работа с корзиной покупок и добавление в избранное.

Каждый ресурс описан в документации: указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, когда это необходимо.

## Как запустить проект:

1. Подготовить виртуальный сервер к развертыванию проекта:

Устанавливаем Docker на удаленном сервере:

```
sudo apt install docker.io 
```

Останавливаем работу nginx (если он запущен):
```
 sudo systemctl stop nginx 
```

Устанавливаем Docker-Compose:
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```
```
sudo chmod +x /usr/local/bin/docker-compose
```
Проверяем, что Docker-Compose установлен:
```
docker-compose --version
```

2. Делаем Fork данного проекта.

3. Добавляем необходимые переменные в GitHub Action Variables:
Список переменных:

```
DB_ENGINE - Тип базы данных default='django.db.backends.postgresql' 
DB_HOST - Хости БД default='db'
DB_NAME - Имя базы данных default='postgres'
DB_PORT - Порт БД default=5432
POSTGRES_USER - Имя пользователя БД default='postgres'
POSTGRES_PASSWORD - Пароль к БД default='postgres'
DOCKER_USERNAME - Имя пользователя в DockerHub
DOCKER_PASSWORD - Пароль к DockerHub

HOST - IP для подключения по SSH к виртуальному серверу
SSH_KEY - Приватный SSH ключ, который имеет доступ к серверу
PASSPHRASE - Пароль для SSH ключа
USER - Имя пользователя виртуального сервера

TELEGRAM_TO - ID телеграм аккаунта для сообщения об успешном деплое
TELEGRAM_TOKEN - Токен телеграм бота
```

4. Делаем пуш в мастер ветку или запускаем Re-run all jobs в Github Actions.

Если все прошло успешно, то в ТГ придет сообщение о деплое и проект запустится на сервере.

## Пример запроса

Все примеры доступны в документации:
```
http://{host}/api/docs/
```
## Стек технологий
- Django REST Framework
- библиотека django-filter
- библиотека Djoser
- git
- postgres

## Автор
Корчагин Павел - https://github.com/pavelkor91
