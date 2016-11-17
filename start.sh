#!/bin/bash

# gunicorn -c /home/box/web/etc/hello.py hello:app --daemon
# gunicorn -c /home/box/web/etc/django.py wsgi --daemon
gunicorn -c /home/box/web/hello.py hello:app --daemon
gunicorn -c /home/box/web/ask/ask wsgi:application --daemon
