from django.contrib import admin
from ..models import DailyConfirmedCase


@admin.register(DailyConfirmedCase)
class DailyConfirmedCaseAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_field", "total", "country")
