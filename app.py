import os, sys
from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

import coloredlogs, logging
coloredlogs.install()

from main.apis.user import api as User
from main.apis.book import api as Book
from main import db_config

# Init app
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

# Swagger UI config
app.config.SWAGGER_UI_JSONEDITOR = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='API docs',
    description='A simple REST API with user authentication.',
)

print(dir(db_config))
# print(db_config)

# @app.before_first_request
# def create_tables():
#     db.create_all()

# Endpoints
api.add_namespace(User, path='/v1')
api.add_namespace(Book, path='/v1')

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
