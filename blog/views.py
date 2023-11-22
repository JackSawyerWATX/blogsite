# blog/views.py

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.models import Post, Comment
from blog.forms import CommentForm
from .models import Visitor

def home(request):
    # Retrieve the visitor count from the database
    visitor_count = Visitor.objects.first().count
    return render(request, 'index.html', {'blog': visitor_count})

def visitor_count(request):
    # Retrieve the visitor count from the database
    visitor_count = Visitor.objects.first().count
    return render(request, 'blog/index.html', {'blog': visitor_count})

def reset_count(request):
    if request.method == 'POST':
        # Reset the visitor count
        Visitor.objects.update(count=0)
        return redirect('home')

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post,
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": CommentForm(),
    }
    return render(request, "blog/detail.html", context)