#!/bin/sh

python manage.py makemigrations
python manage.py migrate
gunicorn todoapp.wsgi:application -c gunicorn_config.py
