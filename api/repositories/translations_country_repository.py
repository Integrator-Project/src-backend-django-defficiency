from django.core.exceptions import ObjectDoesNotExist
from api.models import TranslationsCountry
from api.requests.translations_country_request import TranslationsCountryRequest


def save_translation(translations_request: TranslationsCountryRequest):
    try:
        translation = TranslationsCountry.objects.get(country=translations_request.country.id)
        return False, translation
    except ObjectDoesNotExist:
        translation = TranslationsCountry.create(translations_request)
        translation.save()
        return True, translation
