from django.db import models

from utils import auto_str
from .daily import Daily
from ..apps import ApiConfig


class DailyCase(Daily):
    pass

    class Meta:
        app_label = ApiConfig.name
        db_table = f'{app_label}.daily_case'
