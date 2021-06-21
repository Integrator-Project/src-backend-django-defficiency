from django.db import models
from .daily import Daily
from ..apps import ApiConfig


class DailyRecoveredPeople(Daily):
    pass

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.daily_recovered_people'
