from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from api.models import Country, VaccineApplication
from api.requests import CountryVaccinationDataRequest


def when_started_vaccination_by_country(alpha2_code):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT 
                MIN(date_field) AS 'INICIO VACINACAO' FROM `api.vaccine_application` v
            INNER JOIN
                `api.country` c ON (c.id = v.country_id)
            WHERE
                c.alpha2_code = %s
        ''', [alpha2_code])
        row = cursor.fetchone()

    return row


def save_vaccine_application(
        request: CountryVaccinationDataRequest,
        country: Country,
        vaccines: list):
    try:
        vaccine_application = VaccineApplication.objects.get(date_field=request.date, country=country)
        return False, vaccine_application
    except ObjectDoesNotExist:
        vaccine_application = VaccineApplication.createByRequest(request, country)
        vaccine_application.save()
        vaccine_application.addMultipleVaccines(vaccines)
        return True, vaccine_application
