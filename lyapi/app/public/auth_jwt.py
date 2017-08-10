import jwt, datetime, time
from flask import jsonify
from app.db.table import TableUser
from app.model import ModelUser
from  app.public.common import trueReturn, falseReturn

SECKET_KEY = "dsfsdfsdxcvxfhbsdgfzxcvxc"
class Auth():
    """
    http://www.thatyou.cn/flask-pyjwt-%E5%AE%9E%E7%8E%B0%E5%9F%BA%E4%BA%8Ejson-web-token%E7%9A%84%E7%94%A8%E6%88%B7%E8%AE%A4%E8%AF%81%E6%8E%88%E6%9D%83/
    """
    @staticmethod
    def encode_auth_token(user_id, login_time):
        try:
            payload = {
                "exp":datetime.datetime.utcnow()+datetime.timedelta(days=0, seconds=10),
                "iat": datetime.datetime.utcnow(),
                "iss": "ken",
                "data":{
                    "id": user_id,
                    "login_time":login_time
                }

            }
            return jwt.encode(
                payload,
                SECKET_KEY,
                algorithm="HS256"
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        try:
            payload = jwt.decode(auth_token, SECKET_KEY, options={'verify_exp': False})
            if ('data' in payload and 'id' in payload['data']):
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return "Toekn过期"
        except jwt.InvalidTokenError:
            return "无效Token"

    def authenticate(self, username, password):
        """
        用户登陆，登陆成功返回token，将登陆时间写入数据库，登陆失败返回失败原因
        :param username: 
        :param password: 
        :return: json
        """
        user = ModelUser().find()
        if (user is None):
            return jsonify(falseReturn("","找不到用户"))
        else:
            if (user.check_password(password)):
                login_time = int(time.time())
                user.login_time = login_time
                # self.session.commit(user)
                token = self.encode_auth_token(user.id,login_time)
                return jsonify(trueReturn(token.decode(),'登陆成功'))
            else:
                return jsonify(falseReturn("", "密码不正确"))

    def identity(self, request):
        """
        用户鉴权
        :param request: 
        :return: list
        """
        auth_header = request.headers.get("Authorization")
        if (auth_header):
            auth_tokenArr = auth_header.split(" ")
            if (not auth_tokenArr or auth_tokenArr[0] !="JWT" or len(auth_tokenArr)!=2):
                result = falseReturn("","请传递正确的验证头信息")
            else:
                auth_token = auth_tokenArr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload,str):
                    user = ModelUser().get()
                    if (user is None):
                        result = falseReturn("","找不到该用户信息")
                    else:
                        if (user.login_time == payload["data"]["login_time"]):
                            result = trueReturn(user.id, "请求成功")
                        else:
                            result = falseReturn("","Token已更改，请重新登陆")
                else:
                    result = falseReturn('', payload)
        else:
            result = falseReturn("","没有提供认证token")
        return result
