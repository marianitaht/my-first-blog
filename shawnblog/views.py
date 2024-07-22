# shawnblog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    postdois = Post.objects.all()  # Corrige 'Object' a 'objects'
    return render(request, 'shawnblog/post_list.html', {'posts': postdois})

def bebidas(request):
    postdois = Post.objects.all()  # Corrige 'Object' a 'objects'
    return render(request, 'shawnblog/bebidas.html', {'posts': postdois})





