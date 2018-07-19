"""
Define routes for web app

:author: Almer Mendoza <mamerisawesome@github.com>
"""
from src.init import app
from src.controllers.entities import Item, User

@app.route('/favicon.ico')
def favi():
    return ''

@app.route('/', methods=['GET'])
def index():
    """Return data for landing page"""
    return 'Hello World!'

app.route(User)
app.route(Item)
