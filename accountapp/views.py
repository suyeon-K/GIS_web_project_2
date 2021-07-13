from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import NewModel


def hello_world(request):
    if request.method == "GET":
        return render(request, 'accountapp/hello_world.html',
                      context={'text':"GET METHOD"})
    else:

        temp = request.POST.get('input_text')

        model_instance = NewModel()
        model_instance.text = temp
        model_instance.save()

        data_list = NewModel.objects.all()

        return render(request, 'accountapp/hello_world.html',
                      context={"data_list": data_list})
