from django.db import models
from .entity import Entity
from ..apps import ApiConfig


class Vaccine(Entity):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.vaccine'
