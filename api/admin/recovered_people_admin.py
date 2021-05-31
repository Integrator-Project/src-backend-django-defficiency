from django.contrib import admin
from ..models import RecoveredPeople


@admin.register(RecoveredPeople)
class RecoveredPeopleAdmin(admin.ModelAdmin):
    list_display = ("id", "enabled", "date_time", "total", "country")
