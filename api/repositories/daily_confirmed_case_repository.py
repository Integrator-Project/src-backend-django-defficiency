from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from api.models import DailyConfirmedCase
from django.db import connection
from api.requests.daily_request import DailyRequest


def select_total_confirmed_per_month(alpha2_code, last_months):
    with connection.cursor() as cursor:
        if alpha2_code is not None:
            cursor.execute('''
                SELECT
                    cc.total,
                    cc.date_field
                FROM
                    `api.daily_confirmed_case` cc
                INNER JOIN
                    `api.country` c ON (cc.country_id = c.id) 
                WHERE
                    c.alpha2_code = %s
                    AND date_field BETWEEN DATE_ADD(NOW(), INTERVAL %s MONTH) AND NOW() 
                    AND date_field IN (SELECT
                                        CONCAT(ano, '-', mes, '-', dia)
                                    FROM (SELECT 
                                        MONTH(cc.date_field) as mes,
                                        YEAR(cc.date_field) as ano,
                                        MAX(DAY(cc.date_field)) as dia 
                                        FROM
                                            `api.daily_confirmed_case` cc
                                        INNER JOIN
                                            `api.country` c ON (cc.country_id = c.id) 
                                        WHERE
                                            c.alpha2_code = %s
                                        GROUP BY 1, 2) as ultimo)
                                    ORDER BY date_field
            ''', [alpha2_code, -int(last_months), alpha2_code])
        else:
            cursor.execute('''
                        SELECT
                            SUM(cc.total),
                            cc.date_field
                        FROM
                            `api.daily_confirmed_case` cc
                        INNER JOIN
                            `api.country` c ON (cc.country_id = c.id) 
                        WHERE
                            date_field BETWEEN DATE_ADD(NOW(), INTERVAL %s MONTH) AND NOW() 
                            AND date_field IN (SELECT
                                                CONCAT(ano, '-', mes, '-', dia)
                                            FROM (SELECT 
                                                MONTH(cc.date_field) as mes,
                                                YEAR(cc.date_field) as ano,
                                                MAX(DAY(cc.date_field)) as dia 
                                                FROM
                                                    `api.daily_confirmed_case` cc
                                                INNER JOIN
                                                    `api.country` c ON (cc.country_id = c.id) 
                                                GROUP BY 1, 2) as ultimo)
                         GROUP BY cc.date_field
                         ORDER BY date_field
            ''', [-int(last_months)])

        row = cursor.fetchall()

    return row


def select_total_confirmed(country):
    with connection.cursor() as cursor:
        if country is not None:
            cursor.execute('''
                SELECT
                    SUM(total),
                    date_field
                FROM
                    `api.daily_confirmed_case` v
                INNER JOIN
                    `api.country` c ON (c.id = v.country_id)
                WHERE
                    date_field = (SELECT max(date_field) FROM `api.daily_confirmed_case`)
                    AND c.alpha2_code = %s
            ''', [country])
        else:
            cursor.execute('''
                SELECT
                    SUM(total),
                    date_field
                FROM
                    `api.daily_confirmed_case` v
                WHERE
                    date_field = (SELECT max(date_field) FROM `api.daily_confirmed_case`)
            ''')

        row = cursor.fetchone()

    return row


def select_all_confirmed_global():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(total),
                date_field
            FROM
                `api.daily_confirmed_case` 
            WHERE
                date_field = (SELECT max(date_field) FROM `api.daily_confirmed_case`)
        ''')

        row = cursor.fetchone()

    return row


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
