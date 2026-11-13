from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler
from rest_framework.response import Response

class BaseAPIException(APIException):
    code = 10000
    message = "服务端未知错误"
    @classmethod
    def get_message(cls):
        return {"code": cls.code, "message": cls.message}


class AuthenticationFailedException(BaseAPIException):
    code = 40001
    message = "用户名或者密码错误"


class NotAuthenticatedException(BaseAPIException):
    code = 40002
    message = "用户未登陆，请登录后操作."

class InvalidTokenException(BaseAPIException):
    code = 40003
    message = "非法的 token or token 已经过期,请重新获取."


exc_map = {
    "AuthenticationFailed": AuthenticationFailedException,
    "NotAuthenticated": NotAuthenticatedException,
    "InvalidToken": InvalidTokenException,
}

def global_exception_handler(exc, context):
    print("*"*50)
    print(type(exc), exc.__dict__.items())
    print("*" * 50)
    data = exc_map.get(exc.__class__.__name__, BaseAPIException).get_message()
    response=Response(data)
    return response