from django.contrib import admin
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
    path('', views.base, name='Dashboard'),
    path('Dashboard/', views.base, name='Dashboard'),
    path('Formulario/', views.Formulario, name='Formulario'),
    path('Lista/', views.Lista, name='Lista'),
    path('Ajuda/', views.Ajuda, name='Ajuda'),
    path('ChatBot/', views.ChatBot, name='Chatbot'),
    path('Importar/', views.Importar, name='Importar'),
    path('Teste/', views.Teste, name='Teste'),
]