from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import connection
from api.models import DailyRecoveredPeople
from api.requests.daily_request import DailyRequest


def select_total_recovered_per_month(alpha2_code):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                rp.total,
                rp.date_field
            FROM
                `api.daily_recovered_people` rp
            INNER JOIN
                `api.country` c ON (rp.country_id = c.id) 
            WHERE
                c.alpha2_code = %s
                AND date_field IN (SELECT
                                    CONCAT(ano, '-', mes, '-', dia)
                                FROM (SELECT 
                                    MONTH(rp.date_field) as mes,
                                    YEAR(rp.date_field) as ano,
                                    MAX(DAY(rp.date_field)) as dia 
                                    FROM
                                        `api.daily_recovered_people` rp
                                    INNER JOIN
                                        `api.country` c ON (rp.country_id = c.id) 
                                    WHERE
                                        c.alpha2_code = %s
                                    GROUP BY 1, 2) as ultimo)
                                ORDER BY date_field
        ''', [alpha2_code, alpha2_code])

        row = cursor.fetchall()

    return row


def select_all_recovered_country(country):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(total),
                date_field
            FROM
                `api.daily_recovered_people` v
            INNER JOIN
                `api.country` c ON (c.id = v.country_id)
            WHERE
                date_field = (SELECT max(date_field) FROM `api.daily_recovered_people`)
                AND c.alpha2_code = %s
        ''', [country])

        row = cursor.fetchone()

    return row


def select_all_recovered_global():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(total),
                date_field
            FROM
                `api.daily_recovered_people` 
            WHERE
                date_field = (SELECT max(date_field) FROM `api.daily_recovered_people`)
        ''')

        row = cursor.fetchone()

    return row


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
