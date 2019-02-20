from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from app.db_support import Database 
db = Database()
from app import routes



