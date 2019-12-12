from django import forms
from .models import ModeloFormulario
from django.forms import ModelForm, Textarea

class Formulario(forms.ModelForm):
    class Meta:
        model= ModeloFormulario
        fields= ["Assunto", "Pergunta", "Resposta"]
        widgets = {
            'Pergunta': Textarea(attrs={'cols': 10, 'rows': 4}),
            'Resposta': Textarea(attrs={'cols': 10, 'rows': 4}),
        }
        labels = {
            'Assunto': 'Assunto:',
            'Pergunta': 'Pergunta do Cliente',
            'Resposta': 'Resposta do Bot',
        }