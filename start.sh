#!/bin/bash

gunicorn -c /home/box/web/hello.py hello:app --daemon
gunicorn -c /home/box/web/ask/ask/wsgi.py wsgi:application --daemon
#cd /home/box/web
#sudo gunicorn -b 0.0.0.0:8000 hello:app &
#cd /home/box/web/ask/ask
#sudo gunicorn -b 0.0.0.0:8000 wsgi:application &
