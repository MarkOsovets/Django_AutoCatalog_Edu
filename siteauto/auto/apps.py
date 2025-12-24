from django.apps import AppConfig


class AutoConfig(AppConfig):
    verbose_name = "Семейные авто"
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auto'
