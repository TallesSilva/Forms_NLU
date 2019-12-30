from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import FormFormulario
from .models import ModelFormulario
from django.views.generic import ListView
from django.utils import timezone
import openpyxl

def base(request):
    template = loader.get_template('Dashboard.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def Formulario(request):
    if request.method == 'POST':
        form = FormFormulario(request.POST)
        print(form)
        if form.is_valid():
            ModelFormulario(
                Assunto=form.cleaned_data['Assunto'],
                Pergunta=form.cleaned_data['Pergunta'],
                Resposta=form.cleaned_data['Resposta']
            ).save()
            return HttpResponseRedirect('')
    else:    
        form = FormFormulario()
    return render(request, 'Formulario.html', {'form': form})



def Lista(request):
    try:
        template = loader.get_template('Lista.html')
        NLU = open("Kyros-FAQ/data/nlu.md", 'w')
        NLU.write('\n')
        Resposes = open("Kyros-FAQ/data/responses.md", 'w')
        Resposes.write('\n')
        if request.POST.get('Remove'):
            formularios = request.POST.getlist('formularios')
            for formulario in formularios:
                ModelFormulario.objects.filter(id=formulario).delete()
        elif request.POST.get('Criar'):
            formularios = request.POST.getlist('formularios')
            for formulario in formularios:
                objects = ModelFormulario.objects.get(id=formulario)
                NLU = open("Rasa/nlu.md", 'a')
                NLU.write('\n')
                NLU.write('## intent: {}\n' .format(objects.Assunto))
                for item in objects.Pergunta.split("\n"):
                    NLU.write('- {}' .format(item))
            for formulario in formularios:
                objects = ModelFormulario.objects.get(id=formulario)
                Resposes = open("Rasa/responses.md", 'a')
                Resposes.write('\n')
                Resposes.write('## {}\n' .format(objects.Assunto))
                Resposes.write('* {}\n' .format(objects.Assunto))
                Resposes.write(' - {}\n' .format(objects.Resposta))
        object_list = ModelFormulario.objects.all()
        context = {
            'object_list': object_list,
        }
        
        return HttpResponse(template.render(context, request))
    except:
        template = loader.get_template('Dashboard.html')
        return HttpResponseRedirect(template.render(context, request))

def Ajuda(request):
    template = loader.get_template('Ajuda.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def ChatBot(request):
    template = loader.get_template('ChatBot.html')
    context = {
    }
    return HttpResponse(template.render(context, request))

def Importar(request):
    try:
        template = loader.get_template('Importar.html')
        context = {
        }
        if request.method == 'POST':
            excel_file = request.FILES["excel_file"]
            wb = openpyxl.load_workbook(excel_file)
            ws = wb.active
            return HttpResponse(template.render(context, request))
        elif request.method == "GET":
            return HttpResponse(template.render(context, request))
    except:
        template = loader.get_template('Importar.html')
        context = {
        }
        return HttpResponse(template.render(context, request))
    #ncell = ws.cell(nrow, ncolumn).value
    

    return HttpResponse(template.render(context, request))

def Teste(request):
    template = loader.get_template('teste.html')
    context = {
    }
    return HttpResponse(template.render(context, request))
