from django.contrib import admin
from ..models import DailyCase


@admin.register(DailyCase)
class DailyCaseAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_time", "total", "country")
