from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets as meviewsets
from rest_framework.decorators import action

from .models import (
    Form
)

from .serializers import (
    FormSerializer
)

class FormViewSet(meviewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Form.objects.all()
    serializer_class = FormSerializer

