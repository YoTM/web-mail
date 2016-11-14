import cgi, os

def app(environ, start_response):
    """ Попытка написать wsgi-приложение"""
    query = os.environ.get('QUERY_STRING')
    pairs = cgi._parseparam(query)
    # for key, value in pairs.items():
    #    print(key, value)
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain')
    ]
    start_response(status, response_headers)
    return pairs.items() #iter([data])
