from django.db import models
from .entity import Entity
from .country import Country
from ..apps import ApiConfig
from ..requests.translations_country_request import TranslationsCountryRequest


class TranslationsCountry(Entity):
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    de = models.CharField(max_length=100, null=True, blank=True)
    es = models.CharField(max_length=100, null=True, blank=True)
    fr = models.CharField(max_length=100, null=True, blank=True)
    ja = models.CharField(max_length=100, null=True, blank=True)
    it = models.CharField(max_length=100, null=True, blank=True)
    br = models.CharField(max_length=100, null=True, blank=True)
    pt = models.CharField(max_length=100, null=True, blank=True)
    nl = models.CharField(max_length=100, null=True, blank=True)
    hr = models.CharField(max_length=100, null=True, blank=True)
    fa = models.CharField(max_length=100, null=True, blank=True)

    @classmethod
    def create(cls, request: TranslationsCountryRequest):
        return cls(
            country=request.country,
            de=request.de,
            es=request.es,
            fr=request.fr,
            ja=request.ja,
            it=request.it,
            br=request.br,
            pt=request.pt,
            nl=request.nl,
            hr=request.hr,
            fa=request.fa
        )

    class Meta:
        app_label = ApiConfig.name
        verbose_name_plural = "translation countries"
        db_table = f'{app_label}.translation_country'
