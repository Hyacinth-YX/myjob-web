from django.urls import path
from . import views

urlpatterns = [
    path('jobs', views.jobs),
    path('tags', views.tags),
    path('personality', views.personality),
    path('wage', views.wage),
    path('major', views.major),
    path('ageSex', views.ageSex),
    path('task', views.tags),
    path('hollandCode', views.hollandCode)
]