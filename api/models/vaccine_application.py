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

    def __str__(self):
        return f"DATE_TIME: {self.date_time}\n" \
               f"VACCINATED_PEOPLE: {self.vaccinated_people}\n" \
               f"FULL_VACCINATED_PEOPLE: {self.full_vaccinated_people}\n" \
               f"SOURCE_URL: {self.source_url}\n"

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.vaccine_application'
