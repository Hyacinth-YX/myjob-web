from django.urls import path
from . import views

urlpatterns = [
    path('users', views.users),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('isLogin', views.isLogin),
    path('setToken', views.setToken)
]