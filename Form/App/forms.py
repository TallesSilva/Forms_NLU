from django import forms
from .models import modelsForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.views.generic import CreateView

class formsForm(forms.ModelForm):
    class Meta:
        model= modelsForm
        fields= ["Assunto", "Pergunta", "Resposta"]
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Enviar'))