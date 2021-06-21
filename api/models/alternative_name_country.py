from api.apps import ApiConfig
from api.models import Country
from django.db import models
from api.models.alternative_name import AlternativeName


class AlternativeNameCountry(AlternativeName):
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)

    class Meta:
        app_label = ApiConfig.name
        verbose_name_plural = "alternative name countries"
        db_table = f'{app_label}.alternative_name_country'
