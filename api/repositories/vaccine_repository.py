from django.core.exceptions import ObjectDoesNotExist
from api.models import Vaccine, AlternativeNameVaccine


def save_vaccines(vaccines_request):
    vaccines = list()

    for vaccine_request in vaccines_request.replace(' ', '').split(','):
        _, vaccine = save_vaccine(vaccine_request)
        vaccines.append(vaccine)

    return vaccines


def save_vaccine(vaccine):
    try:
        vaccine = Vaccine.objects.get(name=vaccine)
        return False, vaccine
    except ObjectDoesNotExist:
        try:
            alt_name = AlternativeNameVaccine.objects.get(alternative_name=vaccine)
            return False, alt_name.vaccine
        except ObjectDoesNotExist:
            vaccine = Vaccine.objects.create_by_request(name=vaccine)
            vaccine.save()
            return True, vaccine
