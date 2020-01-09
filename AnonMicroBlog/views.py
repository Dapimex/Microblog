from django.shortcuts import render
from .models import PostModel
from .forms import PostForm


def index(request):
    if request.method == "GET":
        form = PostForm
        posts = PostModel.objects.all()
        return render(request, 'AnonMicroBlog/home.html', {'values': posts, 'form': form})
    elif request.method == "POST":
        form = PostForm(request.POST)
        post = form.save(commit=False)
        post.save()
        posts = PostModel.objects.all()
        form = PostForm
        return render(request, 'AnonMicroBlog/home.html', {'values': posts, 'form': form})
