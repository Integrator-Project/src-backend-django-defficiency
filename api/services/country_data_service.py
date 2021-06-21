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
