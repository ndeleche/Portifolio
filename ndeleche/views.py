from django.shortcuts import render

# home


def index(request):
    return render(request, 'index.html')
