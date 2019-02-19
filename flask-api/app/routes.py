from app import app
from app import api

class apiVersion(Resource):
    def get(self):
        return { 'api-version' : 1.0 }
