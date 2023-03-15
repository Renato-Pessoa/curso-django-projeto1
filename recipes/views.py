from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    context = {
        'name': 'Renato Pessoa'
    }

    return render(request, 'recipes/home.html', context)

def contact(request):
    return HttpResponse("Contact")

def about(request):
    return HttpResponse("About")