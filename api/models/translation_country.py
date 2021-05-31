from django.db import models
from .entity import Entity
from .country import Country
from ..apps import ApiConfig


class TranslationsCountry(Entity):
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    de = models.CharField(max_length=100)
    es = models.CharField(max_length=100)
    fr = models.CharField(max_length=100)
    ja = models.CharField(max_length=100)
    it = models.CharField(max_length=100)
    br = models.CharField(max_length=100)
    pt = models.CharField(max_length=100)
    nl = models.CharField(max_length=100)
    hr = models.CharField(max_length=100)
    fa = models.CharField(max_length=100)

    def __str__(self):
        return f"DE: {self.de}\n" \
               f"ES: {self.es}\n" \
               f"FR: {self.fr}\n" \
               f"JA: {self.ja}\n" \
               f"IT: {self.it}\n" \
               f"BR: {self.br}\n" \
               f"PT: {self.pt}\n" \
               f"NL: {self.nl}\n" \
               f"HR: {self.hr}\n" \
               f"FA: {self.fa}\n"

    class Meta:
        app_label = ApiConfig.name
        verbose_name_plural = "translation countries"
        db_table = f'{app_label}.translation_country'