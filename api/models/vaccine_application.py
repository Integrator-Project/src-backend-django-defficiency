from django.db import models
from .entity import Entity
from .country import Country
from .vaccine import Vaccine
from ..apps import ApiConfig


class VaccineApplication(Entity):
    date_time = models.DateTimeField()
    vaccinated_people = models.IntegerField()
    full_vaccinated_people = models.IntegerField()
    source_url = models.URLField()
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    vaccine = models.ManyToManyField(to=Vaccine)

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.vaccine_application'
