import requests
import environ
import json
from api.requests import CountryVaccinationDataRequest

env = environ.Env()
url = env('GITHUB_REPO_COUNTRY_DATA_URL')


def get_content_country_vaccination():
    response = requests.get(url)
    list_country_data = json.loads(response.content)
    return [CountryVaccinationDataRequest(**x) for x in list_country_data]

