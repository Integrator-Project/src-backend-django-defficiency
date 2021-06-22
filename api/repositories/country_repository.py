from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import connection
from django.db.models import Q
from api.requests import CountryDataRequest
from ..models import Country, AlternativeNameCountry


def world_population():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(c.population)
            FROM `api.country` c
        ''')

        row = cursor.fetchone()

    return row


def get_countries_with_slug():
    return Country.objects.raw('''
        SELECT * FROM `api.country`
            WHERE slug_api IS NOT NULL
    ''')


def get_country_by_alpha2(alpha2: str):
    return Country.objects.get(alpha2_code=alpha2)


def get_country_by_name(name: str):
    try:
        return Country.objects.get(name=name)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        try:
            return Country.objects.get(
                Q(name__icontains=name) |
                Q(name__icontains=name[:round(len(name) / 2)]) |
                Q(name__icontains=name[-round(len(name) / 2):])
            )
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            alt_name = AlternativeNameCountry.objects.get(alternative_name=name)
            return alt_name.country


def save_country(country: CountryDataRequest):
    try:
        country = Country.objects.get(alpha2_code=country.alpha2_code)
        return False, country
    except ObjectDoesNotExist:
        country = Country.createFromRequest(country)
        country.save()
        return True, country
