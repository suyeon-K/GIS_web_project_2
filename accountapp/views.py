from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    if request.method == "GET":
        return render(request, 'accountapp/hello_world.html',
                      context={'text':"GET METHOD"})
    else:
        return render(request, 'accountapp/hello_world.html',
                      context={"text":"POST METHOD"})
