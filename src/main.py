from flask import Flask
from flask_restful_swagger_2 import Api
from flask_cors import CORS
from api.hello import Hello

app = Flask(__name__)

CORS(app)
api = Api(app, title='Blockchain', api_version='1.0.0')
api.add_resource(Hello, '/')
