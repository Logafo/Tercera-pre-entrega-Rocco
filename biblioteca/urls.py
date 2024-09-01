from django.urls import path
from . import views

# Lista de rutas (URLs) de la aplicación "biblioteca"
urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página principal
    path('lista_libros/', views.lista_libros, name='lista_libros'),  # Muestra la lista de libros
    path('lista_autores/', views.lista_autores, name='lista_autores'),  # Muestra la lista de autores
    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),  # Muestra la lista de categorías
    path('lista_prestamos/', views.lista_prestamos, name='lista_prestamos'),  # Muestra la lista de préstamos
    path('crear_libro/', views.crear_libro, name='crear_libro'),  # Ruta para crear un nuevo libro
    path('crear_autor/', views.crear_autor, name='crear_autor'),  # Ruta para crear un nuevo autor
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),  # Ruta para crear una nueva categoría
    path('crear_prestamo/', views.crear_prestamo, name='crear_prestamo'),  # Ruta para registrar un nuevo préstamo
    path('editar_libro/<int:libro_id>/', views.editar_libro, name='editar_libro'),  # Ruta para editar un libro específico
    path('editar_autor/<int:autor_id>/', views.editar_autor, name='editar_autor'),  # Ruta para editar un autor específico
    path('editar_categoria/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),  # Ruta para editar una categoría específica
    path('editar_prestamo/<int:prestamo_id>/', views.editar_prestamo, name='editar_prestamo'),  # Ruta para editar un préstamo específico
    path('eliminar_libro/<int:libro_id>/', views.eliminar_libro, name='eliminar_libro'),  # Ruta para eliminar un libro específico
    path('eliminar_autor/<int:autor_id>/', views.eliminar_autor, name='eliminar_autor'),  # Ruta para eliminar un autor específico
    path('eliminar_categoria/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),  # Ruta para eliminar una categoría específica
    path('eliminar_prestamo/<int:prestamo_id>/', views.eliminar_prestamo, name='eliminar_prestamo'),  # Ruta para eliminar un préstamo específico
]