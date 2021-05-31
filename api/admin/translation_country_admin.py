from django.contrib import admin
from ..models import TranslationsCountry


@admin.register(TranslationsCountry)
class TranslationsCountryAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "country")
