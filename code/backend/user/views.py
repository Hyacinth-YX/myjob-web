from django.middleware.csrf import get_token
import json
from .models import User
from utils.http import HttpWrapper
from utils.errors import NoUser, DuplicateUser, PasswordIncorrect, MethodError


@HttpWrapper
def login(request):
    if request.session.get('is_login', None):
        return {'result': 'logged'}
    if request.method == "POST":
        body_data = json.loads(request.body)
        username = body_data.get('username', None).strip()
        password = body_data.get('password', None).strip()
        if username and password:  # 确保用户名和密码都不为空
            try:
                user = User.objects.get(name=username)
            except:
                raise NoUser
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return {'result': 'success'}
            else:
                raise PasswordIncorrect
    else:
        raise MethodError


@HttpWrapper
def register(requests):
    if requests.method == "POST":
        try:
            post_body = json.loads(requests.body)
            userName = post_body.get('userName')
            password = post_body.get('password')
            email = post_body.get('email')
            User.objects.get(name=userName)
            raise DuplicateUser
        except:
            try:
                User.objects.create(
                    name=userName, password=password, email=email)
                return {'result': 'add user successfully'}
            except Exception as e:
                raise e


@HttpWrapper
def logout(request):
    if not request.session.get('is_login', False):
        return {'result': 'Nothing happen', "is_login": False}
    request.session.flush()
    return {"result": "success", "is_login": request.session.get('is_login', False)}


@HttpWrapper
def setToken(request):
    get_token(request)
    return {'result': True}


@HttpWrapper
def isLogin(request):
    return {'result': request.session.get('is_login', False)}


@HttpWrapper
def users(requests):
    pass
