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


class ListDataForm(ListView):
    model = modelsForm
    paginate_by = 10  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
