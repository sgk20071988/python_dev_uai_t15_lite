from django.shortcuts import redirect, render

from .forms import PostForm
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect("blog:post_list")   # после сохранения — на главную
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", {"form": form})