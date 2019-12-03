import requests
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from tablib import Dataset
from django.shortcuts import render
from json import loads, dumps
from .forms import formsForm
from .models import modelsForm
from django.views.generic import ListView


def Form(request):
    if request.method == 'POST':
        form = formsForm(request.POST)
        if form.is_valid():
            modelsForm(
                Assunto = form.cleaned_data['Assunto'],
                Pergunta = form.cleaned_data['Pergunta'],
                Resposta = form.cleaned_data['Resposta']
            ).save()
            print(modelsForm.objects.all().first())
            return HttpResponseRedirect('')
    else:
        form = formsForm()
    return render(request, 'Form.html', {'form': form})

def List(request):
    template = loader.get_template('List.html')
    form = modelsForm.objects.all()
    context = {
        'form' : form,
    }
    return HttpResponse(template.render(context, request))
