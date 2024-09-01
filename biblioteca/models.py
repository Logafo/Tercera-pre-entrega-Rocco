from django.db import models

# Modelo para guardar info de los autores
class Autor(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre del autor
    nacionalidad = models.CharField(max_length=100)  # Nacionalidad del autor
    fecha_nacimiento = models.DateField()  # Fecha de nacimiento

    def __str__(self):
        return self.nombre  # Muestra el nombre del autor como texto representativo

# Modelo para las categorías de los libros
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)  # Nombre de la categoría
    descripcion = models.TextField()  # Descripción de la categoría

    def __str__(self):
        return self.nombre  # Muestra el nombre de la categoría como texto representativo

# Modelo para guardar info de los libros
class Libro(models.Model):
    titulo = models.CharField(max_length=200)  # Título del libro
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Relación con el autor
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)  # Relación con la categoría, puede ser nula
    fecha_publicacion = models.DateField()  # Fecha de publicación del libro

    def __str__(self):
        return self.titulo  # Muestra el título del libro como texto representativo

# Modelo para registrar los préstamos de libros
class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)  # Relación con el libro
    prestado_a = models.CharField(max_length=100)  # Nombre de la persona a quien se presta
    fecha_prestamo = models.DateField()  # Fecha en que se prestó el libro
    fecha_devolucion = models.DateField()  # Fecha en que se debe devolver el libro

    def __str__(self):
        return f"Préstamo de {self.libro} a {self.prestado_a}"  # Muestra un texto representativo para el préstamo
