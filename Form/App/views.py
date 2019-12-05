from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import Formulario
from .models import ModeloFormulario
from django.views.generic import ListView
from django.utils import timezone

def base(request):
    template = loader.get_template('Dashboard.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def Form(request):
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():
            ModeloFormulario(
                Assunto=form.cleaned_data['Assunto'],
                Pergunta=form.cleaned_data['Pergunta'],
                Resposta=form.cleaned_data['Resposta']
            ).save()
            print(ModeloFormulario.objects.all().first())
            return HttpResponseRedirect('')
    else:
        form = Formulario()
    return render(request, 'Formulario.html', {'form': form})



def List(request):
    template = loader.get_template('ListaFormulario.html')
    object_list = ModeloFormulario.objects.all()
    context = {
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))


def Ajuda(request):
    template = loader.get_template('Ajuda.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

