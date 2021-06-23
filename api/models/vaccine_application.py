from datetime import datetime
from django.db import models
from .entity import Entity
from .country import Country
from .vaccine import Vaccine
from ..apps import ApiConfig
from ..requests import CountryVaccinationDataRequest


class VaccineApplication(Entity):
    date_field = models.DateField()
    total_vaccinations = models.BigIntegerField()
    people_vaccinated = models.BigIntegerField()
    people_fully_vaccinated = models.BigIntegerField()
    source_url = models.URLField(max_length=1000)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name='applications')
    vaccine = models.ManyToManyField(to=Vaccine)

    def addMultipleVaccines(self, vaccines):
        for vaccine in vaccines:
            self.vaccine.add(vaccine)

    @classmethod
    def createByRequest(cls, request: CountryVaccinationDataRequest, country: Country):
        return cls(
            date_field=datetime.strptime(request.date, '%Y-%m-%d'),
            total_vaccinations=request.total_vaccinations,
            people_vaccinated=request.people_vaccinated,
            people_fully_vaccinated=request.people_fully_vaccinated,
            source_url=request.source_url,
            country=country,
        )

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.vaccine_application'
