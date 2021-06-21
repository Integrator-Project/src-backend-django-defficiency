from django.contrib import admin
from ..models import AlternativeNameCountry


@admin.register(AlternativeNameCountry)
class AlternativeNameCountryAdmin(admin.ModelAdmin):
    list_display = ("id", "alternative_name", "enabled", "country")
