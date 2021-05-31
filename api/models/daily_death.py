from django.db import models
from .daily import Daily
from ..apps import ApiConfig


class DailyDeath(Daily):
    pass

    def __str__(self):
        return f"DATE: {self.date_time}\n" \
               f"TOTAL: {self.total}\n"

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.daily_death'
