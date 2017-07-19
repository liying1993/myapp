from flask import g
from flask_cors import cross_origin
from flask_restful import Resource
from app.model import ModelUser

class ResourceUser(Resource):

    @cross_origin()
    def get(self):
        result = ModelUser().find()
        if result:
            return "yes!"
        return "hello world"
