from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.models import DailyConfirmedCase
from api.requests.daily_request import DailyRequest


def save_daily_confirmed_list(requests):
    daily_cases = list()

    for request in requests:
        _, daily_case = save_daily_confirmed(request)
        daily_cases.append(daily_case)

    return daily_cases


def save_daily_confirmed(request: DailyRequest):
    try:
        daily_case = DailyConfirmedCase.objects.get(
            date_field=request.date_field,
            country=request.country)

        return False, daily_case
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        daily_case = DailyConfirmedCase.create_by_request(request)
        daily_case.save()
        return True, daily_case
