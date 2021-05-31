from django.db import models
from .entity import Entity
from .continent import Continent
from ..apps import ApiConfig


class Country(Entity):
    name = models.CharField(max_length=100)
    alpha_2_code = models.CharField(max_length=2)
    alpha_3_code = models.CharField(max_length=3)
    capital = models.CharField(max_length=100)
    continent = models.ForeignKey(to=Continent, on_delete=models.CASCADE, related_name="countries")
    region = models.CharField(max_length=100)
    sub_region = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.FloatField()
    native_name = models.CharField(max_length=100)
    flag = models.URLField()
    numeric_code = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'NAME: {self.name}'

    class Meta:
        app_label = ApiConfig.name
        verbose_name_plural = "countries"
        db_table = f'{app_label}.country'