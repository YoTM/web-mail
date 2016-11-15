#!/usr/bin/env python
# -*- coding: utf-8 -*-

def app(environ, start_response):
    """ Ф-я парсит аргументы из урла
        и преобразует в словарь
    """
    resp = environ['QUERY_STRING'].split('&')
    resp = [item+'\r\n' for item in resp]
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    start_response(status, headers)

return resp
