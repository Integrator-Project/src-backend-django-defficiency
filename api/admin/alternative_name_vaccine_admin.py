from django.contrib import admin
from ..models import AlternativeNameVaccine


@admin.register(AlternativeNameVaccine)
class AlternativeNameVaccineAdmin(admin.ModelAdmin):
    list_display = ("id", "alternative_name", "enabled", "vaccine")
