from flask import g
from flask_cors import cross_origin
from app.public import decorate_body_params,decorate_resource
from flask_restful import Resource
from app.model import ModelUser

class ResourceUser(Resource):

    @cross_origin()
    @decorate_resource()
    @decorate_body_params(params_except=["telephone", "password"])
    def get(self):
        pass


    @cross_origin()
    @decorate_resource()
    @decorate_body_params(params_except=["telephone", "password"])
    def post(self):
        try:
            result = ModelUser().find_by_telephone(g.params["telephone"])
            if result:
                user = ModelUser().create(g.params["telephone"], g.params["password"])
                return {"msg": "success"}

        except Exception:
            print("lalal")
