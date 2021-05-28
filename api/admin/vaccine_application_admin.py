from django.contrib import admin
from ..models import VaccineApplication


@admin.register(VaccineApplication)
class VaccineApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_time", "vaccinated_people",
                    "full_vaccinated_people", "source_url", "country")
