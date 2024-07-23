# mysite/urls.py
from django.contrib import admin
from django.urls import path
from shawnblog import views  # Asegúrate de importar las vistas desde tu aplicación

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post_list/', views.post_list, name='post_list'),
    path('bebidas/', views.bebidas_view, name='bebidas'),  # Usa el nombre correcto de la vista
]

