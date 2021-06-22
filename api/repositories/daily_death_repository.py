from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import connection
from api.models import DailyDeath
from api.requests.daily_request import DailyRequest


def select_total_death_per_month(alpha2_code):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                dd.total,
                dd.date_field
            FROM
                `api.daily_death` dd
            INNER JOIN
                `api.country` c ON (dd.country_id = c.id) 
            WHERE
                c.alpha2_code = %s
                AND date_field IN (SELECT
                                    CONCAT(ano, '-', mes, '-', dia)
                                FROM (SELECT 
                                    MONTH(dd.date_field) as mes,
                                    YEAR(dd.date_field) as ano,
                                    MAX(DAY(dd.date_field)) as dia 
                                    FROM
                                        `api.daily_death` dd
                                    INNER JOIN
                                        `api.country` c ON (dd.country_id = c.id) 
                                    WHERE
                                        c.alpha2_code = %s
                                    GROUP BY 1, 2) as ultimo)
                                ORDER BY date_field
        ''', [alpha2_code, alpha2_code])

        row = cursor.fetchall()

    return row


def select_all_death_country(country):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(total),
                date_field
            FROM
                `api.daily_death` v
            INNER JOIN
                `api.country` c ON (c.id = v.country_id)
            WHERE
                date_field = (SELECT max(date_field) FROM `api.daily_death`)
                AND c.alpha2_code = %s
        ''', [country])

        row = cursor.fetchone()

    return row


def select_all_death_global():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(total),
                date_field
            FROM
                `api.daily_death` 
            WHERE
                date_field = (SELECT max(date_field) FROM `api.daily_death`)
        ''')

        row = cursor.fetchone()

    return row


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
