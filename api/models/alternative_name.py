from api.apps import ApiConfig
from api.models import Entity
from django.db import models


class AlternativeName(Entity):
    alternative_name = models.CharField(max_length=255)

    class Meta:
        app_label = ApiConfig.name
        abstract = True
