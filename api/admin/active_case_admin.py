from django.contrib import admin
from ..models import ActiveCase


@admin.register(ActiveCase)
class ActiveCaseAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_time", "total", "country")
