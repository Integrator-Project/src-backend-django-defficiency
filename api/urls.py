from django.urls import include, path
from rest_framework import routers
from .views import *

api_router = routers.DefaultRouter()

api_router.register(r"active-case", ActiveCaseViewSet)
api_router.register(r"continent", ContinentViewSet)
api_router.register(r"country", CountryViewSet)
api_router.register(r"daily-case", DailyCaseViewSet)
api_router.register(r"daily-death", DailyDeathViewSet)
api_router.register(r"recovered-people", RecoveredPeopleViewSet)
api_router.register(r"translation-country", TranslationsCountryViewSet)
api_router.register(r"vaccine-application", VaccineApplicationViewSet)
api_router.register(r"vaccine", VaccineViewSet)

urlpatterns = [
    path("", include(api_router.urls))
]
