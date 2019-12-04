from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', views.base, name='index'),
    path('Formulario/', views.Form, name='Formulario'),
    path('Lista/', views.List, name='Lista'),
]