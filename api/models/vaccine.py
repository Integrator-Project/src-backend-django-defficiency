from django.db import models
from .entity import Entity
from ..apps import ApiConfig


class Vaccine(Entity):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    producer = models.CharField(max_length=255, null=True, blank=True)
    CAS_number = models.CharField(max_length=100, null=True, blank=True)
    drug_bank = models.CharField(max_length=100, null=True, blank=True)
    UNII = models.CharField(max_length=100, null=True, blank=True)
    KEGG = models.CharField(max_length=100, null=True, blank=True)
    pub_chem_SID = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.vaccine'
