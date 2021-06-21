from django.db import models
from .entity import Entity
from ..apps import ApiConfig
from ..requests import CountryDataRequest


class Country(Entity):
    name = models.CharField(max_length=100)
    alpha2_code = models.CharField(max_length=2)
    alpha3_code = models.CharField(max_length=3)
    slug_api = models.CharField(null=True, blank=True, max_length=100)
    capital = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    sub_region = models.CharField(max_length=100)
    population = models.IntegerField()
    area = models.FloatField(null=True, blank=True, default=0.0)
    native_name = models.CharField(max_length=100)
    flag = models.URLField()
    numeric_code = models.IntegerField(null=True, blank=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    @classmethod
    def createFromRequest(cls, request: CountryDataRequest):
        latitude = 0
        longitude = 0

        try:
            latitude = request.latlng[0]
            longitude = request.latlng[1]
        except IndexError:
            pass

        return cls(
            name=request.name,
            alpha2_code=request.alpha2_code,
            alpha3_code=request.alpha3_code,
            capital=request.capital,
            region=request.region,
            sub_region=request.subregion,
            population=request.population,
            area=request.area,
            native_name=request.native_name,
            flag=request.flag,
            numeric_code=request.numeric_code,
            latitude=latitude,
            longitude=longitude
        )

    class Meta:
        app_label = ApiConfig.name
        verbose_name_plural = "countries"
        db_table = f'{app_label}.country'
