from django.contrib import admin
from ..models import DailyActiveCase


@admin.register(DailyActiveCase)
class DailyActiveCaseAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_field", "total", "country")
