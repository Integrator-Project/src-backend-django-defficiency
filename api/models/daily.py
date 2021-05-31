from django.db import models
from .entity import Entity
from .country import Country
from ..apps import ApiConfig


class Daily(Entity):
    date_time = models.DateTimeField()
    total = models.IntegerField()
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)

    class Meta:
        app_label = ApiConfig.name
        abstract = True
