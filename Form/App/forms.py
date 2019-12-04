from django import forms
from .models import modelsForm

class formsForm(forms.ModelForm):
    class Meta:
        model= modelsForm
        fields= ["Assunto", "Pergunta", "Resposta"]
