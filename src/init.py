"""
Initialize Flask app

:author: Almer Mendoza <mamerisawesome@github.com>
"""

from src.app import create_app
import src.config as config

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

import os

config_object = eval(os.environ['FLASK_APP_CONFIG'])
app = create_app(config_object)
