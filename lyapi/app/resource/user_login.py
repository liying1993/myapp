from flask import g
from flask_cors import cross_origin
from app.public import decorate_body_params, decorate_resource
from flask_restful import Resource
from app.model import ModelUser
import hashlib
import os

class ResourceUserLogin(Resource):

    @cross_origin()
    @decorate_resource()
    @decorate_body_params(params_except=["telephone", "password"])
    def post(self):
        user = ModelUser().find_a_user(g.params["telephone"])
        if user.check_password(g.params["password"]):
            accessToken = "user"+hashlib.sha1(os.urandom(24)).hexdigest()
            ModelUser().update_access_token(user.id, accessToken)
            return {"user_id": user.id,"accessToken":accessToken}
