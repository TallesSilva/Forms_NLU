from rest_framework_mongoengine import serializers
from drf_queryfields import QueryFieldsMixin

from .models import (
    Form )
    
class FormSerializer(QueryFieldsMixin, serializers.DocumentSerializer):
    class Meta:
        model = Form
        fields = '__all__'
