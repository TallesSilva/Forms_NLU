from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('Formulario/', views.Form, name='Formulario'),
    path('Lista/', views.List, name='Lista'),
]