#!/bin/bash

# дальше идёт моя попытка автоматизации создания заготовки приложений

sudo django-admin startproject ask
echo "created ask django-project"
cd ask
sudo chmod +x manage.py
sudo ./manage.py startapp qa
echo "created qa app"
