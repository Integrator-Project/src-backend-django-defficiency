from datetime import datetime
from django.db import models
from .entity import Entity
from .country import Country
from ..apps import ApiConfig
from ..requests.daily_request import DailyRequest


class Daily(Entity):
    date_field = models.DateField(default=datetime.now)
    total = models.IntegerField()
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)

    @classmethod
    def create_by_request(cls, request: DailyRequest):
        return cls(
            date_field=request.date_field,
            total=request.total,
            country=request.country
        )

    class Meta:
        app_label = ApiConfig.name
        abstract = True
