import requests

from django.http import HttpResponse
from django.template import loader
from .models import modelsForm
from tablib import Dataset
from django.shortcuts import render
from json import loads, dumps
from .forms import formsForm
from django.views.generic import CreateView


def Form(request):
    form= formsForm(request.POST)
    if form.is_valid():
        form.save()

    context= {'form': form }
        
    return render(request, 'Form.html', context)
