from django.urls import path
from . import views

urlpatterns = [
    path('recommendJob', views.recommendJob),
    path('recordBigjob', views.recordBigjob),
    path('recordJob', views.recordJob)
]