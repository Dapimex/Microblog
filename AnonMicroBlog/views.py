from django.shortcuts import render

posts = []


def index(request):
    return render(request, 'home.html', {'values': posts})
