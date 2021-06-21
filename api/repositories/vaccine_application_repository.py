from django.core.exceptions import ObjectDoesNotExist
from api.models import Country, VaccineApplication
from api.requests import CountryVaccinationDataRequest


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
