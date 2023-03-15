from django.shortcuts import render

def home(request):

    context = {
        'name': 'Renato Pessoa'
    }

    return render(request, 'recipes/home.html', context)

def contact(request):
    return render(request, 'recipes/contact.html')
