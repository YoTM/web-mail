#!/bin/bash

gunicorn -c /home/box/web/hello.py hello:app --daemon
gunicorn -c /home/box/web/ask/ask/wsgi.py wsgi:application --daemon
