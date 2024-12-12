from django.apps import AppConfig


class CardimportConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cardImport"

    def ready(self): #Connects the "signal so that when an import request is created it is processed
        from . import reciever
