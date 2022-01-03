from django.http import HttpResponse
from utils.errors import *
import json


def HttpWrapper(func):
    def exception2message(exception):
        if isinstance(exception, NoValue):
            result = [1, "数值错误"]
        elif isinstance(exception, DuplicateUser):
            result = [2, "重复的用户名"]
        elif isinstance(exception, MethodError):
            result = [3, "请求方法错误"]
        elif isinstance(exception, NoUser):
            result = [4, "用户不存在"]
        elif isinstance(exception, PasswordIncorrect):
            result = [5, "密码错误"]
        else:
            result = [1000, "Error:"]
        result[1] += str(exception)
        return result

    def Wrapped(*args, **kwargs):
        try:
            return_value = func(*args, **kwargs)
            if return_value == None:
                return_value = []
        except Exception as e:
            return_value = e
        keys = ["code", "message", "data"]
        if isinstance(return_value, Exception):
            values = exception2message(return_value) + [[]]
        else:
            values = [0, "success", return_value]
        response = dict([keys[i], values[i]] for i in range(3))
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
        response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return HttpResponse(json.dumps(response))
    return Wrapped
