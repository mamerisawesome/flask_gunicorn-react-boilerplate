"""
Server main runner

:author: Almer Mendoza <mamerisawesome@github.com>
"""

from src.controllers.routes import app

if __name__ == "__main__":
    app.run(host= '0.0.0.0')
