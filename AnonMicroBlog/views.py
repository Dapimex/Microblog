from django.shortcuts import render
from AnonMicroBlog.models import PostModel

posts = PostModel.objects.all()


def index(request):
    if request.method == "GET":
        return render(request, 'home.html', {'values': posts})
    elif request.method == "POST":
        return render(request, 'home.html', {'values': posts})


