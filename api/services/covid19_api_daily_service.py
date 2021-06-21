import requests
import environ
import json
from datetime import datetime
from humps import decamelize
from ..repositories import get_countries_with_slug, save_daily_actives, save_daily_recovered_list
from ..requests import Covid19CountryDataRequest
from ..requests.daily_request import DailyRequest

env = environ.Env()
covid19_api = 'COVID19_API'


def post_global_all():
    _, _, recovered, active = get_global_daily_data()
    save_daily_recovered_list(recovered)
    save_daily_actives(active)


def get_global_daily_data():
    countries = get_countries_with_slug()
    confirmed, deaths, recovered, active = (list() for _ in range(4))

    for country in countries:
        response = requests.get(f"{env(covid19_api)}/live/country/{country.slug_api}")
        data_list = decamelize(json.loads(response.content))
        countries_data = [Covid19CountryDataRequest(**x) for x in data_list]

        for data in countries_data:
            date_field = datetime.strptime(data.date, '%Y-%m-%dT%H:%M:%SZ')
            # confirmed.append(DailyRequest(country=country, total=data.confirmed, date_field=date_field))
            # deaths.append(DailyRequest(country=country, total=data.deaths, date_field=date_field))
            recovered.append(DailyRequest(country=country, total=data.recovered, date_field=date_field))
            active.append(DailyRequest(country=country, total=data.active, date_field=date_field))

    return confirmed, deaths, recovered, active
