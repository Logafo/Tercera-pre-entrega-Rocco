"""
Django settings for mi_biblioteca project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Definición del directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Idioma y formato de fecha
LANGUAGE_CODE = 'es'  # Idioma español
DATE_INPUT_FORMATS = ['%d/%m/%Y']  # Definir formato de entrada de fecha: dd/mm/aaaa

# Clave secreta (se debe mantener en secreto en producción)
SECRET_KEY = 'django-insecure--!@$m0iwk2s_co9kqg&c)xihc54f)p(dhshhu!sbyt!ogq028*'

# Depuración (True para desarrollo, False para producción)
DEBUG = False

# Hosts permitidos (vacío para desarrollo local)
ALLOWED_HOSTS = ['tercera-pre-entrega-rocco-production.up.railway.app']

# Aplicaciones instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'biblioteca',  # Nuestra aplicación principal
]

# Middleware (mecanismos que procesan peticiones/respuestas)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de la URL raíz
ROOT_URLCONF = 'mi_biblioteca.urls'

# Configuración de plantillas
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ruta a la carpeta de plantillas
        'APP_DIRS': True,  # Activa la búsqueda automática de plantillas en las aplicaciones
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicación WSGI
WSGI_APPLICATION = 'mi_biblioteca.wsgi.application'

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validadores de contraseñas
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configuración de internacionalización
LANGUAGE_CODE = 'es'  # Cambiado a español
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True  # Activar la localización para formatear números y fechas
USE_TZ = True

# Archivos estáticos (CSS, JavaScript, Imágenes)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Tipo de campo de clave primaria predeterminado
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
