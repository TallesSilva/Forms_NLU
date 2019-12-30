from django import forms
from .models import ModelFormulario
from django.forms import ModelForm, Textarea

class FormFormulario(forms.ModelForm):
    class Meta:
        model= ModelFormulario
        fields= ["Assunto", "Pergunta", "Resposta"]
