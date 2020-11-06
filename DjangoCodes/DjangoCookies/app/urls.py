from django.urls import path
from . import views

urlpatterns = [
    path('', views.setCookie, name='index'),
    path('show', views.getCookie, name='show')
]