#!/bin/bash
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
gunicorn -c /home/box/web/etc/django.py wsgi --daemon
# дальше идёт моя попытка автоматизации создания заготовки приложений

sudo django-admin startproject ask
echo "created ask django-project"
sudo cd ask
sudo chmod +x manage.py
sudo ./manage.py startapp qa
echo "created qa app"
