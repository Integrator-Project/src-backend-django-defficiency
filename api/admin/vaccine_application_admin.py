from django.contrib import admin
from ..models import VaccineApplication


@admin.register(VaccineApplication)
class VaccineApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_field", "people_vaccinated",
                    "people_fully_vaccinated", "source_url", "country")
