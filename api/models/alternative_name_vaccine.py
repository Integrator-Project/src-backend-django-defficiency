from api.apps import ApiConfig
from api.models import Vaccine
from django.db import models
from api.models.alternative_name import AlternativeName


class AlternativeNameVaccine(AlternativeName):
    vaccine = models.ForeignKey(to=Vaccine, on_delete=models.CASCADE, related_name='alternative_names')

    class Meta:
        app_label = ApiConfig.name
        verbose_name_plural = "alternative name vaccines"
        db_table = f'{app_label}.alternative_name_vaccine'
