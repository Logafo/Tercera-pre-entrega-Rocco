from django.contrib import admin
from .models import Autor, Categoria, Libro, Prestamo

# Registramos los modelos para que aparezcan en el panel de administración de Django
admin.site.register(Autor)       # Hace que el modelo Autor sea visible y editable desde el admin
admin.site.register(Categoria)   # Hace que el modelo Categoria sea visible y editable desde el admin
admin.site.register(Libro)       # Hace que el modelo Libro sea visible y editable desde el admin
admin.site.register(Prestamo)    # Hace que el modelo Prestamo sea visible y editable desde el admin
