from django.apps import AppConfig

import base


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'

    # def  ready(self):
    #     return base.signals