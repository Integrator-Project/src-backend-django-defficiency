from sys import stdout
import requests
import pandas as pd
from io import StringIO
from django.db.models import QuerySet
from .github_data_service import get_content_data_repo
from ..repositories import *

country_data = 'GITHUB_REPO_COUNTRY_DATA_URL'


def get_all_vaccine_application_by_country(country_id) -> QuerySet[VaccineApplication]:
    # country = Country.objects.get(id=country_id)
    return VaccineApplication.objects.filter(country=country_id)


def post_vaccine_application():
    country_content_data = get_content_data_repo(country_data)

    for i in country_content_data:
        csv = requests.get(i.download_url).content
        df = pd.read_csv(StringIO(csv.decode("UTF-8")), sep=',').fillna(0)
        values = [CountryVaccinationDataRequest(*x) for x in df.values]

        for j in values:
            try:
                country = get_country_by_name(j.location)
                vaccines = save_vaccines(j.vaccine)
                save_vaccine_application(j, country, vaccines)
            except (ObjectDoesNotExist, MultipleObjectsReturned):
                stdout.write(f"{j.location} não está cadastrado.\n")
