import wrapt
from flask import g, request
from app.exception import ExceptionResponse


def decorate_body_params(params_except=None, params_option=None):
    """应用通用参数验证装饰器，若验证成功则将数据写入g.params
    :param
        params_except [list]    Json内的必选参数
        params_option [list]    Json内的可选参数
    """

    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        data = request.json
        g.params = {}
        if params_except is not None:
            if data is None:
                raise ExceptionResponse(401, "参数非法")
            try:
                for key in params_except:
                    g.params[key] = data[key]
            except KeyError:
                raise ExceptionResponse(401, "参数非法")
            try:
                for key in params_option:
                    g.params[key] = data[key]
            except KeyError:
                pass
            except TypeError:
                pass
        if params_option is not None:
            for key in params_option:
                try:
                    g.params[key] = data[key]
                except KeyError:
                    g.params[key] = None
        return wrapped(*args, **kwargs)

    return decorated_function
