 # API сервис проекта YATUBE
 Проект разработан в рамках обучения на курсе Backend-разработчик Яндекс Практикума.
___
### Описание
Это полноценное дополнение проекта YATUBE. Благодаря API данные проекта YATUBE можно получать на различных ресурсах и что самое важное на различных устройствах. Любое мобильное приложение или веб сайт может пользоваться данными YATUBE, вносить изменения и держать в курсе всех подписчиков своих авторов на всех видах устройств, даже в Telegram!
___
### Технологии
- [Python 3.7]
- [Django 3.2.15]
- [SimpleJWT 4.7.2]
- [Django REST Framework 3.12.4]
___
# Запуск проекта в dev-режиме на локальном сервере:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/DmitryRotanin/api_final_yatube.git
```
```
cd api_final_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
Сервер будет доступен по адресу:
```
<http://127.0.0.1:8000/>
```
___
### Примеры запросов
Для получения списка доступных адресов отправьте запрос:
```
<http://127.0.0.1:8000/api/v1/>
```
Для получения всех постов:
```
<http://127.0.0.1:8000/api/v1/posts/>
```
Все виды запросов и их описание доступно в документации по адресу:
```
<http://127.0.0.1:8000/redoc/>
```
___
### Автор
Дмитрий Ротанин, студент Яндекс Практикума

[//]: # (Ниже находятся справочные ссылки)

   [Python 3.7]: <https://www.python.org/downloads/release/python-370/>
   [Django 3.2.15]: <https://www.djangoproject.com/download/>
   [SimpleJWT 4.7.2]: <https://django-rest-framework-simplejwt.readthedocs.io/en/latest/>
   [Django REST Framework 3.12.4]: <https://www.django-rest-framework.org/community/release-notes/>