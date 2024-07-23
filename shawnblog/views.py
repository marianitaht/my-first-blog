# shawnblog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    postdois = Post.objects.all()  # Corrige 'Object' a 'objects'
    return render(request, 'shawnblog/post_list.html', {'posts': postdois})

def bebidas_view(request):
    postdois = Post.objects.all()  # Corrige 'Object' a 'objects'
    return render(request, 'bebidas.html',{'posts': postdois})





