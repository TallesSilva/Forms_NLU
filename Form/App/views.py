from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .forms import formsForm
from .models import modelsForm
from django.views.generic import ListView
from django.utils import timezone

def base(request):
    template = loader.get_template('base.html')
    context = {
    }
    return HttpResponse(template.render(context, request))


def Form(request):
    if request.method == 'POST':
        form = formsForm(request.POST)
        if form.is_valid():
            modelsForm(
                Assunto=form.cleaned_data['Assunto'],
                Pergunta=form.cleaned_data['Pergunta'],
                Resposta=form.cleaned_data['Resposta']
            ).save()
            print(modelsForm.objects.all().first())
            return HttpResponseRedirect('')
    else:
        form = formsForm()
    return render(request, 'Form.html', {'form': form})



def List(request):
    template = loader.get_template('List.html')
    object_list = modelsForm.objects.all()
    context = {
        'object_list': object_list,
    }
    return HttpResponse(template.render(context, request))

