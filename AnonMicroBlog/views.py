from django.shortcuts import render
from .models import PostModel
from .forms import PostForm


def index(request):
    if request.method == "GET":
        form = PostForm
        posts = PostModel.objects.all()
        return render(request, 'home.html', {'values': posts, 'form': form, 'clear': clear_posts})
    elif request.method == "POST":
        form = PostForm(request.POST)
        form.fields["post"] = "Напишите пост"
        post = form.save(commit=False)
        post.save()
        posts = PostModel.objects.all()
        form = PostForm
        return render(request, 'home.html', {'values': posts, 'form': form})


def clear_posts():
    PostModel.objects.all().delete()
    return

