#!/bin/bash
sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

# дальше идёт моя попытка автоматизации создания заготовки приложений

sudo django-admin.py ask
echo "created ask django-proect"
sudo cd ask
sudo ./manage.py startapp qa
echo "created qa app"
