from django.db import models
from .daily import Daily
from ..apps import ApiConfig


class RecoveredPeople(Daily):
    pass

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.recovered_people'
