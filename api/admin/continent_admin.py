from django.contrib import admin
from ..models import Continent


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "name")
