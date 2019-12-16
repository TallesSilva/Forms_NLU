from django import forms
from .models import ModeloFormulario
from django.forms import ModelForm, Textarea

class Formulario(forms.ModelForm):
    class Meta:
        model= ModeloFormulario
        fields= ["Assunto", "Pergunta", "Resposta"]
        widgets = {
            'Pergunta': Textarea(attrs={'cols': 10, 'rows': 4, 'placeholder':'Tente variar ao máximo as perguntas sobre esse assunto e procure não repetir a mesma pergunta ou inserir perguntas cadastradas para outros assuntos'}),
            'Resposta': Textarea(attrs={'cols': 10, 'rows': 4, 'placeholder':'É permitido apenas um tipo de resposta para cada assunto'}),
        }
        labels = {
            'Assunto': 'Assunto:',
            'Pergunta': 'Pergunta do Cliente:',
            'Resposta': 'Resposta do Bot:',
        }