import requests
import environ
import json
from ..models import Country
from api.requests import CountryVaccinationDataRequest, CountryDataRequest
from humps import decamelize

env = environ.Env()


def post_all_countries_data():
    countries = get_all_countries_data()
    converted = [Country() for country in countries]


def get_all_countries_data():
    response = requests.get(f"{env('REST_COUNTRIES')}/all")
    list_countries = decamelize(json.loads(response.content))
    return [CountryDataRequest(**x) for x in list_countries]


def get_content_country_vaccination():
    response = requests.get(env('GITHUB_REPO_COUNTRY_DATA_URL'))
    list_country_data = decamelize(json.loads(response.content))
    return [CountryVaccinationDataRequest(**x) for x in list_country_data]
