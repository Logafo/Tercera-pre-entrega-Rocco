# mi_biblioteca/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para entrar al panel de administración de Django
    path('', include('biblioteca.urls')),  # Incluye todas las rutas definidas en el archivo urls.py de la app "biblioteca"
]
