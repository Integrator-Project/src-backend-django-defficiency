from django.contrib import admin
from ..models import DailyDeath


@admin.register(DailyDeath)
class DailyDeathAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_time", "total", "country")
