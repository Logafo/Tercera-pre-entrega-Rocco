from django.apps import AppConfig


class BibliotecaConfig(AppConfig):
    # Configuración predeterminada para los campos auto generados
    default_auto_field = 'django.db.models.BigAutoField'
    # Nombre de la aplicación que estamos configurando
    name = 'biblioteca'
