from django.urls import include, path
from rest_framework import routers
from .views import *

api_router = routers.DefaultRouter()

api_router.register(r"active-case", DailyActiveCaseViewSet)
api_router.register(r"country", CountryViewSet)
api_router.register(r"daily-case", DailyConfirmedCaseViewSet)
api_router.register(r"daily-death", DailyDeathViewSet)
api_router.register(r"recovered-people", DailyRecoveredPeopleViewSet)
api_router.register(r"translation-country", TranslationsCountryViewSet)
api_router.register(r"vaccine-application", VaccineApplicationViewSet)
api_router.register(r"vaccine", VaccineViewSet)
api_router.register(r"alternative-name-country", AlternativeNameCountryViewSet)
api_router.register(r"alternative-name-vaccine", AlternativeNameVaccineViewSet)

urlpatterns = [
    path("", include(api_router.urls))
]
