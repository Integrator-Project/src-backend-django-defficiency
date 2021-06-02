from django.db import models
from .entity import Entity
from ..apps import ApiConfig


class Vaccine(Entity):
    name = models.CharField(max_length=255)

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.vaccine'
