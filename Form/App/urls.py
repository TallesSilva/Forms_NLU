from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', views.base, name='Dashboard'),
    path('Dashboard/', views.base, name='Dashboard'),
    path('Formulario/', views.Form, name='Formulario'),
    path('Lista/', views.List, name='Lista'),
    path('Ajuda/', views.Ajuda, name='Ajuda'),
    path('teste/', views.teste, name='teste'),
]