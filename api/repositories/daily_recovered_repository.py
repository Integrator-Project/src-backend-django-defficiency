from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.models import DailyRecoveredPeople
from api.requests.daily_request import DailyRequest


def save_daily_recovered_list(requests):
    daily_recovered_list = list()

    for request in requests:
        _, daily_recovered = save_daily_recovered(request)
        daily_recovered_list.append(daily_recovered)

    return daily_recovered_list


def save_daily_recovered(request: DailyRequest):
    try:
        daily_recovered = DailyRecoveredPeople.objects.get(
            date_field=request.date_field,
            country=request.country)

        return False, daily_recovered
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        daily_recovered = DailyRecoveredPeople.create_by_request(request)
        daily_recovered.save()
        return True, daily_recovered
