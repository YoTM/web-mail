#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi, os

def app(environ, start_response):

    """ Попытка написать wsgi-приложение"""
    query = os.environ.get('QUERY_STRING')
    print query
    response_headers = [
        ('Content-type', 'text/plain')
    ]
    start_response(status, response_headers)
    return null
