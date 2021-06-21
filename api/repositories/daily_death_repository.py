from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.models import DailyDeath
from api.requests.daily_request import DailyRequest


def save_daily_deaths(requests):
    daily_deaths = list()

    for request in requests:
        _, daily_death = save_daily_death(request)
        daily_deaths.append(daily_death)

    return daily_deaths


def save_daily_death(request: DailyRequest):
    try:
        daily_case = DailyDeath.objects.get(
            date_field=request.date_field,
            country=request.country)

        return False, daily_case
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        daily_case = DailyDeath.create_by_request(request)
        daily_case.save()
        return True, daily_case
