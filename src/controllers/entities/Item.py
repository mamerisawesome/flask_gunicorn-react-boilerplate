"""
Template RESTful object builder

:author: Almer Mendoza <mamerisawesome@github.com>
"""

from flask import request
from src.init import app

def http_get_all(req):
    """Get method definition"""
    return 'Accessing items'

def http_get(req):
    """Get method definition"""
    return 'Accessing item'

def http_post(req):
    """Post method definition"""
    return 'Creating item'

def http_put(req):
    """Put method definition"""
    return 'Updating item'

def http_del(req):
    """Delete method definition"""
    return 'Deleting item'

@app.route('/item', methods=['GET', 'POST', 'PUT', 'DELETE'])
def items():
    if request.method == 'GET':
        return http_get_all(request)

@app.route('/item/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def item(id):
    if request.method == 'GET' and id is not None:
        return http_get(request)
    elif request.method == 'POST' and id is not None:
        return http_post(request)
    elif request.method == 'PUT' and id is not None:
        return http_put(request)
    elif request.method == 'DELETE' and id is not None:
        return http_del(request)
    else:
        # Return http error 405 method not allowed
        return abort(405)
