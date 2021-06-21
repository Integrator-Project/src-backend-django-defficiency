from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.models import DailyActiveCase
from api.requests.daily_request import DailyRequest


def save_daily_actives(requests):
    daily_actives = list()

    for request in requests:
        _, daily_active = save_daily_active(request)
        daily_actives.append(daily_active)

    return daily_actives


def save_daily_active(request: DailyRequest):
    try:
        daily_active = DailyActiveCase.objects.get(
            date_field=request.date_field,
            country=request.country)

        return False, daily_active
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        daily_active = DailyActiveCase.create_by_request(request)
        daily_active.save()
        return True, daily_active
