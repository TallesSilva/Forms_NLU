from django import forms
from .models import ModeloFormulario
from django.forms import ModelForm, Textarea

class Formulario(forms.ModelForm):
    class Meta:
        model= ModeloFormulario
        fields= ["Assunto", "Pergunta", "Resposta"]
