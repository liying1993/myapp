import wrapt
from flask import Response
import json


def decorate_resource():
    """RESTFul Json标准返回值装饰器，拦截标准异常转化为 HTTP 错误码"""

    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        try:
            data = wrapped(*args, **kwargs)
            resp = Response(json.dumps(data, ensure_ascii=False))
            resp.headers["Content-Type"] = "image/jpeg; charset=UTF-8"
            resp.status_code = 200
            return resp
        except Exception as e:
            if hasattr(e, "http_status") and hasattr(e, "err_msg"):
                resp = Response(json.dumps({"msg": e.err_msg}, ensure_ascii=False))
                resp.headers["Content-Type"] = "text/plain; charset=UTF-8"
                resp.status_code = e.http_status
                return resp
            raise e

    return decorated_function
