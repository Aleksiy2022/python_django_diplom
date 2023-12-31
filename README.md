# Проект Megano
Интернет-магазин Megano.

## Описание
Предтавляет собой подключаемое django-приложение. Берет на себя все что связано с отображением страниц, а обращение 
за данными происходит по API. 

## Контракт для API
Названия роутов и ожидаемую структуру ответа от API endpoints можно найти в `megano/swagger/MeganoAPI.yaml`.

## Установка и запуск проекта

1. Установите Docker на вашей машине, если он еще не установлен. Подробные инструкции доступны по ссылке: 
Docker Installation Guide (https://docs.docker.com/get-docker/)

2. После успешной установки Docker, находясь в корневой дирректории проекта выполните следующую команду, чтобы развернуть проект: `docker compose up`.

Команда загрузит необходимые Docker-образы (если они еще не были загружены), загрузит необходимые зависимости для 
проекта, выполнит миграции для базы данных, создаст контейнеры для присутствующих сервисов, включая Celery, Flower, 
RabbitMQ, настроит и запустит их в соответствии с файлом `docker-compose.yml`, который находится в корневой директории 
проекта. Вы можете открыть его и настроить параметры по своему усмотрению.

Страртовая страница доступна по адресу 'http://127.0.0.1:8000/'

Для доступа к Административной панели необходимо создать суперпользователя: `python manage.py createsuperuser`

## Компоненты проекта

Проект использует следующие компоненты:

- Celery: асинхронная очередь задач.
- Flower: визуальная панель управления для Celery. Доступен по адресу: 'http://127.0.0.1:5555/'
- RabbitMQ: посредник сообщений. Доступен по адресу: 'http://127.0.0.1:15672/'  Username: guest Password: guest


### Использование фикстур
Фикстуру с тестовыми данными можно найти в `megano/fixtures/megano_data.json`.
Если вы хотите заполнить базу тестовыми данными, воспользуйтесь командой находясь в директории `.megano/`: `python manage.py loaddata fixtures/megano_data.json`

#### В указанной тестовой базе 3 пользователя:

| Роль пользователя | user      | password  |
|-------------------|-----------|-----------|
| superuser         | admin     | !1234QWER |
| user              | Aleksey   | !1234QWER |
| user              | Aleksandr | !1234QWER |
