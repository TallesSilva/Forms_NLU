from django.conf.urls import url
from rest_framework import routers
from rest_framework_mongoengine import routers as merouters

from .views import *


merouter = merouters.DefaultRouter()
merouter.register(r'form', FormViewSet, basename='Form')
urlpatterns = []
urlpatterns += merouter.urls