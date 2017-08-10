import wrapt
from flask import g, request
from app.exception import ExceptionResponse
from app.model import  ModelUser


def auth_permission(permission_model):
    """权限 Access Token 验证装饰器
    在accestoken前面加上一个标志位置，其中user表示普通用户登陆，admin表示管理员登陆

    当 env == "debug" 时，"1024"为万能 AccessToken ，可以用在单元测试的编写上。参考例子为 test/api_user_bc_node_list_get.py
    """

    @wrapt.decorator
    def decorated_function(wrapped, instance, args, kwargs):
        user_id = request.headers.get("UserID")
        accesstoken = request.headers.get("AccessToken")
        g.user_id = user_id
        # 参数检查
        if not user_id or not accesstoken:
            raise ExceptionResponse(401, "参数不合法")
        # 设定权限模式
        if accesstoken.startswith("admin"):
            g.permission_model = "admin"
        elif accesstoken.startswith("agent"):
            g.permission_model = "agent"
        else:
            g.permission_model = "user"
        # 验证鉴权对象的有效性。在 user 模式下，需要将 user 存入 g.user，administrator 模式，也将 g.user 设置为 None（然并卵）。
        if "admin" in permission_model and g.permission_model == "admin":
            admin = auth_administrator(user_id, accesstoken)
            if admin:
                g.admin = admin
            else:
                raise ExceptionResponse(401, "权限不合法")

        elif "user" in permission_model and g.permission_model == "user":
            # 用户模式
            user = auth_user(user_id, accesstoken)

            if user:
                g.user = user
            else:
                raise ExceptionResponse(401, "权限不合法")
        elif "agent" in permission_model and g.permission_model == "agent":
            #agent模式
            agent = auth_agent(user_id, accesstoken)
            if agent:
                g.agent = agent
            else:
                raise ExceptionResponse(401, "权限不合法")
        else:
            raise ExceptionResponse(401, "权限不合法")
        return wrapped(*args, **kwargs)

    return decorated_function


def auth_administrator(user_uid, access_token):
    """验证用户 Access Token
    :return <bool> 鉴权结果
    """
    pass
    # try:
    #     if env == "debug" and access_token == "1024":
    #         result = ModelAdmin().find_by_uid(user_uid)
    #     else:
    #         result = ModelAdmin().find_by_uid_and_token(user_uid, access_token)
    # except FileExistsError:
    #     raise ExceptionResponse(401, "管理员未登陆")
    # return result


def auth_user(user_uid, access_token):
    """验证用户 Access Token
    :return <TableUser> 用户对象
    """
    try:

        result = ModelUser().find_user_by_user_id_and_token(access_token, user_uid)
    except FileExistsError:
        raise ExceptionResponse(401, "用户未登陆")
    return result

def auth_agent(user_uid, access_token):
    pass
    # try:
    #     if env == "debug" and access_token == "1024":
    #         result = ModelAgent().find_by_id(user_uid)
    #     else:
    #         result = ModelAgent().find_by_uid_and_token(user_uid, access_token)
    # except FileExistsError:
    #     raise ExceptionResponse(401, "代理商未登陆")
    # return result