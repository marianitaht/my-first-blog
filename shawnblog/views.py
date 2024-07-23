# shawnblog/views.py
from django.shortcuts import render
from .models import Post
def post_list(request):
    # Aquí debes tener lógica para obtener y pasar datos a la plantilla
    return render(request, 'shawnblog/post_list.html')

def bebidas_view(request):
    # Aquí debes tener lógica para obtener y pasar datos a la plantilla
    return render(request, 'shawnblog/bebidas.html')




