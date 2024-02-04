from django.apps import AppConfig


class BuluntuConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.buluntu'


    def ready(self):
        import apps.buluntu.signals

    