# shawnblog/views.py
from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'shawnblog/post_list.html', {'posts': post_list})

def bebidas_view(request):
    post_list = Post.objects.all()  # Cambia 'Post' por el modelo que estés utilizando
    return render(request, 'bebidas.html', {'posts': post_list})





