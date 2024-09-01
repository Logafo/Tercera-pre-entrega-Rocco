from django.shortcuts import render, redirect, get_object_or_404
from .models import Autor, Categoria, Libro, Prestamo
from .forms import AutorForm, CategoriaForm, LibroForm, PrestamoForm, BuscarLibroForm

# -------------------- Vistas para listar elementos --------------------

def inicio(request):
    # Muestra la página de inicio
    return render(request, 'biblioteca/inicio.html')

def lista_libros(request):
    # Obtiene todos los libros y los muestra
    libros = Libro.objects.all()
    return render(request, 'biblioteca/lista_libros.html', {'libros': libros})

def lista_autores(request):
    # Obtiene todos los autores y los muestra
    autores = Autor.objects.all()
    return render(request, 'biblioteca/lista_autores.html', {'autores': autores})

def lista_categorias(request):
    # Obtiene todas las categorías y las muestra
    categorias = Categoria.objects.all()
    return render(request, 'biblioteca/lista_categorias.html', {'categorias': categorias})

def lista_prestamos(request):
    # Obtiene todos los préstamos y los muestra
    prestamos = Prestamo.objects.all()
    return render(request, 'biblioteca/lista_prestamos.html', {'prestamos': prestamos})

# -------------------- Vistas para crear nuevos elementos --------------------

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    # Muestra el formulario para crear un libro
    return render(request, 'biblioteca/crear_libro.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm()
    # Muestra el formulario para crear un autor
    return render(request, 'biblioteca/crear_autor.html', {'form': form})

def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm()
    # Muestra el formulario para crear una categoría
    return render(request, 'biblioteca/crear_categoria.html', {'form': form})

def crear_prestamo(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm()
    # Muestra el formulario para registrar un préstamo
    return render(request, 'biblioteca/crear_prestamo.html', {'form': form})

# -------------------- Vistas para editar elementos --------------------

def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm(instance=libro)
    # Muestra el formulario para editar un libro
    return render(request, 'biblioteca/crear_libro.html', {'form': form})

def editar_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('lista_autores')
    else:
        form = AutorForm(instance=autor)
    # Muestra el formulario para editar un autor
    return render(request, 'biblioteca/crear_autor.html', {'form': form})

def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=categoria)
    # Muestra el formulario para editar una categoría
    return render(request, 'biblioteca/crear_categoria.html', {'form': form})

def editar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            return redirect('lista_prestamos')
    else:
        form = PrestamoForm(instance=prestamo)
    # Muestra el formulario para editar un préstamo
    return render(request, 'biblioteca/crear_prestamo.html', {'form': form})

# -------------------- Vistas para eliminar elementos --------------------

def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    libro.delete()
    # Redirige a la lista de libros después de eliminar
    return redirect('lista_libros')

def eliminar_autor(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    autor.delete()
    # Redirige a la lista de autores después de eliminar
    return redirect('lista_autores')

def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, pk=categoria_id)
    categoria.delete()
    # Redirige a la lista de categorías después de eliminar
    return redirect('lista_categorias')

def eliminar_prestamo(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    prestamo.delete()
    # Redirige a la lista de préstamos después de eliminar
    return redirect('lista_prestamos')
