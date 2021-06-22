import requests
import environ
import json
from humps import decamelize
from ..repositories import *
from ..requests import Covid19APICountryRequest
from ..requests.translations_country_request import TranslationsCountryRequest

env = environ.Env()
rest_countries = 'REST_COUNTRIES'
covid19_api = 'COVID19_API'


def total_daily_data(alpha2_code):
    if alpha2_code is None:
        from_data = 'World'
        c_value, c_date = select_all_confirmed_global()
        a_value, a_date = select_all_active_global()
        r_value, r_date = select_all_recovered_global()
        d_value, d_date = select_all_death_global()
    else:
        from_data = Country.objects.get(alpha2_code=alpha2_code).name
        c_value, c_date = select_all_confirmed_country(alpha2_code)
        a_value, a_date = select_all_active_country(alpha2_code)
        r_value, r_date = select_all_recovered_country(alpha2_code)
        d_value, d_date = select_all_death_country(alpha2_code)

    return {
        'from': from_data,
        'confirmed': {'value': c_value, 'last_update': c_date},
        'active': {'value': a_value, 'last_update': a_date},
        'recovered': {'value': r_value, 'last_update': r_date},
        'death': {'value': d_value, 'last_update': d_date}
    }


def data_per_month(alpha2_code):
    confirmed = select_total_confirmed_per_month(alpha2_code)
    active = select_total_active_per_month(alpha2_code)
    recovered = select_total_recovered_per_month(alpha2_code)
    death = select_total_death_per_month(alpha2_code)

    return {
        'confirmed': confirmed,
        'active': active,
        'recovered': recovered,
        'death': death
    }


def update_all_countries_slug():
    countries_request = get_all_countries_data_covid19_api()

    for country_request in countries_request:
        try:
            country = get_country_by_iso2(country_request.ISO2)
            country.slug_api = country_request.slug
            country.save()
        except ObjectDoesNotExist:
            print(f"Esse país: {country_request.ISO2}/{country_request.country} não está cadastrado")


def post_all_countries_data():
    countries_request = get_all_countries_data()

    for country_request in countries_request:
        _, country = save_country(country_request)
        save_translation(TranslationsCountryRequest(country, **country_request.translations))


def get_all_countries_data():
    response = requests.get(f"{env(rest_countries)}/all")
    list_countries = decamelize(json.loads(response.content))
    return [CountryDataRequest(**x) for x in list_countries]


def get_all_countries_data_covid19_api():
    response = requests.get(f"{env(covid19_api)}/countries")
    list_countries = decamelize(json.loads(response.content))
    return [Covid19APICountryRequest(**x) for x in list_countries]
