from django.urls import path
from . import views

urlpatterns = [
    path('getPosts', views.getPosts), # jobCat
    path('getPost', views.getPost),  # postId
    path('addPost', views.addPost),  # jobCat
    path('getComments', views.getComments),  # postId
    path('addComment', views.addComment),  # postId
]