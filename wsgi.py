from website.app import create_app
import website.config as config

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import os

config_object = eval(os.environ['FLASK_APP_CONFIG'])
app = create_app(config_object)

if __name__ == "__main__":
    app.run()
