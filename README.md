## FOODGRAM - "Продуктовый помощник"
Сервис позволяет публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список "Избранное", а перед походом в магазин - скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

![workflow](https://github.com/s-palagin/foodgram-project-react/actions/workflows/main.yml/badge.svg)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/) [![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/) [![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/) [![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/) [![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/) [![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/) [![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/) [![Docker-compose](https://img.shields.io/badge/-Docker%20compose-464646?style=flat-square&logo=Docker)](https://www.docker.com/) [![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions) [![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
##  Запуск проекта в Docker контейнере

* Установите Docker.

Параметры запуска описаны в файлах `docker-compose.yml` и `nginx.conf`
* Cоздайте файл `.env` в корневой директории с содержанием:
```
DB_ENGINE=django.db.backends.postgresql
# Укажите имя созданной базы данных
DB_NAME=foodgram
# Укажите имя пользователя
POSTGRES_USER=foodgram_user
# Укажите пароль для пользователя
POSTGRES_PASSWORD=1731Pa
# Укажите localhost
DB_HOST=127.0.0.1
# Укажите порт для подключения к базе
DB_PORT=5432
```
* Запустите docker compose:
```bash
docker-compose up -d --build
```
* Примените миграции:
```bash
docker-compose exec backend python manage.py migrate
```
* Загрузите ингредиенты:
```bash
docker-compose exec backend python manage.py load_ingredients ingredients.json
```
* Создайте администратора:
```bash
docker-compose exec backend python manage.py createsuperuser
```
* Соберите статику:
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```
##  Пользовательские роли в проекте
1. Анонимный пользователь
2. Аутентифицированный пользователь
3. Администратор
###  Анонимные пользователи могут:
1. Просматривать список рецептов;
2. Просматривать отдельные рецепты;
3. Фильтровать рецепты по тегам;
4. Создавать аккаунт.
###  Аутентифицированные пользователи могут:
1. Получать данные о своей учетной записи;
2. Изменять свой пароль;
3. Просматривать, публиковать, удалять и редактировать свои рецепты;
4. Добавлять понравившиеся рецепты в избранное и удалять из избранного;
5. Добавлять рецепты в список покупок и удалять из списка;
6. Подписываться и отписываться на авторов;
7. Скачать список покупок
### Администраторы могут:
1. Получить доступ к административной панели;
2. Изменять пароль любого пользователя;
3. Создавать/блокировать/удалять аккаунты пользователей;
4. Редактировать/удалять  **любые**  рецепты;
5. Добавлять/удалять/редактировать ингредиенты;
6. Добавлять/удалять/редактировать теги.

###  Сайт

Сайт доступен по ссылке:

[Foodgram](http://158.160.12.243/)

Вход в административную зону:
e-mail - test@gmail.com
пароль - testtesttest
*
