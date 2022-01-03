from django import http
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.middleware.csrf import get_token
import json
from .models import User


def login(request):
    if request.session.get('is_login', None):
        return HttpResponse({'code': 0, 'result': 'logged'})
    if request.method == "POST":
        body_data = json.loads(request.body)
        username = body_data.get('username', None).strip()
        password = body_data.get('password', None).strip()
        if username and password:  # 确保用户名和密码都不为空
            try:
                user = User.objects.get(name=username)
            except:
                return HttpResponse(json.dumps({'code': 1, 'result': 'no user'}))
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return HttpResponse(json.dumps({'code': 0, 'result': 'success'}))
            else:
                raise HttpResponse(json.dumps(
                    {'code': 2, 'result': 'password incorrect'}))
    else:
        return HttpResponseBadRequest('Method Error')


def register(requests):
    if requests.method == "POST":
        try:
            post_body = json.loads(requests.body)
            userName = post_body.get('userName')
            password = post_body.get('password')
            email = post_body.get('email')
            User.objects.get(name=userName)
            return HttpResponse(json.dumps({'code': 1, 'result': 'username exist'}))
        except:
            try:
                User.objects.create(
                    name=userName, password=password, email=email)
                return HttpResponse(json.dumps({'code': 0, 'result': 'add user successfully'}))
            except Exception as e:
                return HttpResponse(json.dumps({'code': 2, 'result': f"Error:[{str(e)}]"}))


def logout(request):
    if not request.session.get('is_login', False):
        return HttpResponse(json.dumps({'code': 0, 'result': 'Nothing happen'}))
    request.session.flush()
    return HttpResponse(json.dumps({'code': 0, "result": "success", "temp": request.session.get('is_login', False)}))


def setToken(request):
    get_token(request)
    return HttpResponse(json.dumps({'code': 0, 'result': True}))


def isLogin(request):
    return HttpResponse(json.dumps({'result': request.session.get('is_login', False)}))


def users(requests):
    pass
