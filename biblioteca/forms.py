from django import forms
from .models import Autor, Categoria, Libro, Prestamo

# Formulario para crear o editar un autor
class AutorForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField(
        # Configura el input de fecha para mostrar el formato dd/mm/aaaa
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'}),
        input_formats=['%d/%m/%Y'],  # Formato de fecha aceptado
        label='Fecha de Nacimiento',
        error_messages={
            'required': 'Este campo es obligatorio.',  # Mensaje si el campo está vacío
            'invalid': 'Ingrese una fecha válida (dd/mm/aaaa).'  # Mensaje si el formato de la fecha es incorrecto
        }
    )

    class Meta:
        model = Autor  # Modelo que usa este formulario
        fields = ['nombre', 'nacionalidad', 'fecha_nacimiento']  # Campos del formulario

# Formulario para crear o editar una categoría
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria  # Modelo que usa este formulario
        fields = ['nombre', 'descripcion']  # Campos del formulario
        error_messages = {
            'nombre': {'required': 'Este campo es obligatorio.'},  # Mensaje si el campo nombre está vacío
        }

# Formulario para crear o editar un libro
class LibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(
        # Configura el input de fecha para mostrar el formato dd/mm/aaaa
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'}),
        input_formats=['%d/%m/%Y'],  # Formato de fecha aceptado
        label='Fecha de Publicación',
        error_messages={
            'required': 'Este campo es obligatorio.',  # Mensaje si el campo está vacío
            'invalid': 'Ingrese una fecha válida (dd/mm/aaaa).'  # Mensaje si el formato de la fecha es incorrecto
        }
    )

    class Meta:
        model = Libro  # Modelo que usa este formulario
        fields = ['titulo', 'autor', 'categoria', 'fecha_publicacion']  # Campos del formulario

# Formulario para registrar un préstamo de libro
class PrestamoForm(forms.ModelForm):
    fecha_prestamo = forms.DateField(
        # Configura el input de fecha para mostrar el formato dd/mm/aaaa
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'}),
        input_formats=['%d/%m/%Y'],  # Formato de fecha aceptado
        label='Fecha de Préstamo',
        error_messages={
            'required': 'Este campo es obligatorio.',  # Mensaje si el campo está vacío
            'invalid': 'Ingrese una fecha válida (dd/mm/aaaa).'  # Mensaje si el formato de la fecha es incorrecto
        }
    )
    fecha_devolucion = forms.DateField(
        # Configura el input de fecha para mostrar el formato dd/mm/aaaa
        widget=forms.DateInput(format='%d/%m/%Y', attrs={'type': 'text', 'placeholder': 'dd/mm/aaaa'}),
        input_formats=['%d/%m/%Y'],  # Formato de fecha aceptado
        label='Fecha de Devolución',
        error_messages={
            'required': 'Este campo es obligatorio.',  # Mensaje si el campo está vacío
            'invalid': 'Ingrese una fecha válida (dd/mm/aaaa).'  # Mensaje si el formato de la fecha es incorrecto
        }
    )

    class Meta:
        model = Prestamo  # Modelo que usa este formulario
        fields = ['libro', 'prestado_a', 'fecha_prestamo', 'fecha_devolucion']  # Campos del formulario

# Formulario para buscar un libro por título
class BuscarLibroForm(forms.Form):
    criterio = forms.CharField(
        label='Buscar por título',  # Etiqueta del campo de búsqueda
        max_length=200,  # Máximo de caracteres que se pueden ingresar
        error_messages={
            'required': 'Este campo es obligatorio.',  # Mensaje si no se introduce nada en la búsqueda
        }
    )
