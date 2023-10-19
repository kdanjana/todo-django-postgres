#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
gunicorn todoapp.wsgi:application -c gunicorn_config.py
