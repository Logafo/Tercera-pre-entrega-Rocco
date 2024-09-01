# Proyecto: <img src="https://i.imgur.com/XTt4zIr.png" width="22">LibroManía - Gestión de Biblioteca 


### Alumno: Christian Rocco  
### Comisión: 57830  
### Pre-Entrega #3

## Descripción del Proyecto

**LibroManía** es una aplicación web desarrollada como parte de la pre-entrega del curso de Python en Coderhouse. Esta aplicación permite gestionar libros, autores, categorías y préstamos en una biblioteca. Utiliza el framework Django para proporcionar un entorno robusto y escalable para la administración de la biblioteca.

## Funcionalidades Principales

1. **Gestión de Libros:**
   - Crear, editar, eliminar y listar libros en la biblioteca.
2. **Gestión de Autores:**
   - Crear, editar, eliminar y listar autores.
3. **Gestión de Categorías:**
   - Crear, editar, eliminar y listar categorías.
4. **Gestión de Préstamos:**
   - Registrar, editar, eliminar y listar préstamos de libros.
5. **Interfaz de Usuario Amigable:**
   - Utiliza Bootstrap 4 para una interfaz moderna y responsiva.

## Tecnologías Utilizadas

- **Python**: Lenguaje de programación principal.
- **Django**: Framework web utilizado para desarrollar la aplicación.
- **Bootstrap 4**: Framework CSS para estilizar la interfaz de usuario.
- **SQLite**: Base de datos utilizada en desarrollo.
- **HTML5** y **CSS3**: Para la estructura y estilo de las páginas web.
- **JavaScript**: Para interactividad adicional en la interfaz.

## Requisitos del Sistema

- Python 3.8 o superior
- Django 5.1
- Bootstrap 4

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Logafo/Tercera-pre-entrega-Rocco
   ```
   ```bash
   cd Tercera-pre-entrega-Rocco
   ```

2. **Crea un entorno virtual (Windows):**

   ```bash
   python -m venv venv
   ```
   ```bash
   venv\Scripts\activate
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Inicia el servidor de desarrollo:**

   ```bash
   python manage.py runserver
   ```

5. **Accede a la aplicación:**

   Abre tu navegador y ve a `http://127.0.0.1:8000/`.

## Cómo Utilizar la Aplicación

1. **Página de Inicio:**
   - Introducción al propósito del proyecto y cómo navegar por las secciones.

2. **Gestión de Libros:**
   - Ve a la sección "Libros" para ver la lista de libros existentes, crear uno nuevo, editar o eliminar libros.

3. **Gestión de Autores:**
   - Ve a la sección "Autores" para ver, crear, editar o eliminar autores.

4. **Gestión de Categorías:**
   - Ve a la sección "Categorías" para administrar las diferentes categorías de libros.

5. **Gestión de Préstamos:**
   - Ve a la sección "Préstamos" para registrar nuevos préstamos de libros, así como editar o eliminar los existentes.

## Panel de Administración

El proyecto incluye un panel de administración de Django para gestionar todos los modelos de forma más avanzada.

- **URL del admin:** `http://127.0.0.1:8000/admin/`

Para crear un superusuario y acceder al panel de administración, utiliza el siguiente comando:

```bash
python manage.py createsuperuser
```

## Estructura del Proyecto

```
Tercera-pre-entrega-Rocco/
.
│   .gitignore                      # Archivo para especificar qué archivos y carpetas ignorar en el repositorio
│   db.sqlite3                      # Base de datos SQLite utilizada en el proyecto
│   manage.py                       # Script de Django para comandos de administración
│   README.md                       # Documento de instrucciones y descripción del proyecto
│   requirements.txt                # Listado de dependencias del proyecto
│   
├───biblioteca                      # Carpeta de la aplicación 'biblioteca'
│   │   admin.py                    # Configuración del panel de administración de Django para 'biblioteca'
│   │   apps.py                     # Configuración de la aplicación 'biblioteca'
│   │   forms.py                    # Formularios utilizados en la aplicación
│   │   models.py                   # Definición de modelos de base de datos
│   │   tests.py                    # Pruebas unitarias para la aplicación
│   │   urls.py                     # Definición de rutas (URLs) para la aplicación
│   │   views.py                    # Vistas de la aplicación, controlan la lógica del negocio
│   │   __init__.py                 # Archivo que indica que 'biblioteca' es un paquete Python
│   │   
│   └───migrations                  # Carpeta para archivos de migración de Django
│       │   0001_initial.py         # Primera migración que crea las tablas de base de datos
│       └   __init__.py             # Inicializador de la carpeta de migraciones
│       
├───mi_biblioteca                   # Carpeta del proyecto principal 'mi_biblioteca'
│   │   asgi.py                     # Configuración de ASGI para el proyecto
│   │   settings.py                 # Configuración global del proyecto
│   │   urls.py                     # Rutas globales del proyecto
│   │   wsgi.py                     # Configuración de WSGI para el proyecto
│   └   __init__.py                 # Inicializador de la carpeta del proyecto
│   
├───static                          # Carpeta de archivos estáticos (CSS, imágenes, etc.)
│   │   favicon.ico                 # Ícono del sitio web
│   │   input.png                   # Imagen del logotipo del sitio
│   └   styles.css                  # Hoja de estilos (CSS) para la página
│       
└───templates                       # Carpeta de plantillas HTML
    └───biblioteca                  # Plantillas específicas para la aplicación 'biblioteca'
        │   base.html               # Plantilla base para herencia de otras plantillas
        │   crear_autor.html        # Plantilla para crear un autor
        │   crear_categoria.html    # Plantilla para crear una categoría
        │   crear_libro.html        # Plantilla para crear un libro
        │   crear_prestamo.html     # Plantilla para registrar un préstamo
        │   inicio.html             # Plantilla para la página de inicio
        │   lista_autores.html      # Plantilla para listar autores
        │   lista_categorias.html   # Plantilla para listar categorías
        │   lista_libros.html       # Plantilla para listar libros
        └   lista_prestamos.html    # Plantilla para listar préstamos

```

## Dependencias

El archivo `requirements.txt` incluye todas las bibliotecas necesarias para ejecutar el proyecto:

```
asgiref==3.5.2
Django==5.1
sqlparse==0.4.3
pytz==2024.1
```

## Créditos

- **Christian Rocco** - Desarrollo del proyecto como parte del curso de Python en Coderhouse.