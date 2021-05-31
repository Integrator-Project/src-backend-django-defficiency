from django.db import models
from ..apps import ApiConfig


class Entity(models.Model):
    objects = models.Manager()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=True)

    class Meta:
        app_label = ApiConfig.name
        abstract = True
