from django.shortcuts import render

def home(request):

    context = {
        'name': 'Renato Pessoa'
    }

    return render(request, 'recipes/pages/home.html', context)


