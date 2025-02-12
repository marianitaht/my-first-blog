# mysite/urls.py
from django.contrib import admin
from django.urls import path
from shawnblog import views  # Asegúrate de importar las vistas desde tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bebidas.html/', views.bebidas_view, name='bebidas'),  # Usa 'bebidas_view' en lugar de 'bebidas'
    path('', views.post_list, name='post_list'),
]
