from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import PostForm

def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the requests
        # check whether it's valid:
        form = PostForm(request.method)
        if form.is_valid():
            print(form)
            return HttpResponseRedirect('')
        else:
            return HttpResponseRedirect('')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})



