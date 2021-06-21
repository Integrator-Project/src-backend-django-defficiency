from sys import stdout as out
import requests
from io import StringIO
import pandas as pd
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from .github_data_service import get_content_data_repo
from ..repositories import get_country_by_name, get_countries_with_slug
from ..repositories.daily_confirmed_case_repository import save_daily_confirmed_list
from ..repositories.daily_death_repository import save_daily_deaths
from ..requests.daily_request import DailyRequest

time_series = 'CSSE_COVID19_TIME_SERIES'
daily_death_name = 'time_series_covid19_deaths_global.csv'
daily_case_name = 'time_series_covid19_confirmed_global.csv'
country_region = 'Country/Region'


def post_global_daily_death():
    daily_death_requests = get_global_daily(daily_death_name)
    return save_daily_deaths(daily_death_requests)


def post_global_daily_case():
    daily_case_requests = get_global_daily(daily_case_name)
    return save_daily_confirmed_list(daily_case_requests)


def get_global_daily(daily_type: str):
    request_list = list()
    repo_data = get_content_data_repo(time_series)
    daily_death_obj = next(x for x in repo_data if x.name == daily_type)

    csv = requests.get(daily_death_obj.download_url).content
    df = pd.read_csv(StringIO(csv.decode("UTF-8")), sep=',')\
        .fillna(0)\
        .groupby([country_region])\
        .sum()\
        .reset_index()

    columns = list(df.iloc[:, 3:])
    dates = [datetime.strptime(x, '%m/%d/%y') for x in columns]

    for i in df.values:
        try:
            country = get_country_by_name(i[0])
            count = 3
            for j in dates:
                request = DailyRequest(
                    country=country,
                    total=i[count],
                    date_field=j
                )

                request_list.append(request)
                count += 1
        except ObjectDoesNotExist:
            out.write(f"{i[0]} não está cadastrado.\n")

    return request_list
