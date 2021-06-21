from django.contrib import admin
from ..models import DailyRecoveredPeople


@admin.register(DailyRecoveredPeople)
class DailyRecoveredPeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_field", "total", "country")
