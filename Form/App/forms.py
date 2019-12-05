from django import forms
from .models import ModeloFormulario

class Formulario(forms.ModelForm):
    class Meta:
        model= ModeloFormulario
        fields= ["Assunto", "Pergunta", "Resposta"]
