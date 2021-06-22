from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import connection
from api.models import DailyActiveCase
from api.requests.daily_request import DailyRequest


def select_total_active_per_month(alpha2_code, last_months):
    with connection.cursor() as cursor:
        if alpha2_code is not None:
            cursor.execute('''
                SELECT
                    ac.total,
                    ac.date_field
                FROM
                    `api.daily_active_case` ac
                INNER JOIN
                    `api.country` c ON (ac.country_id = c.id) 
                WHERE
                    c.alpha2_code = %s
                    AND date_field BETWEEN DATE_ADD(NOW(), INTERVAL %s MONTH) AND NOW() 
                    AND date_field IN (SELECT
                                        CONCAT(ano, '-', mes, '-', dia)
                                    FROM (SELECT 
                                        MONTH(ac.date_field) as mes,
                                        YEAR(ac.date_field) as ano,
                                        MAX(DAY(ac.date_field)) as dia 
                                        FROM
                                            `api.daily_active_case` ac
                                        INNER JOIN
                                            `api.country` c ON (ac.country_id = c.id) 
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
                            `api.daily_active_case` cc
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
                                                    `api.daily_active_case` cc
                                                INNER JOIN
                                                    `api.country` c ON (cc.country_id = c.id) 
                                                GROUP BY 1, 2) as ultimo)
                         GROUP BY cc.date_field
                         ORDER BY date_field
            ''', [-int(last_months)])

        row = cursor.fetchall()

    return row


def select_total_active(country):
    with connection.cursor() as cursor:
        if country is not None:
            cursor.execute('''
                SELECT
                    SUM(total),
                    date_field
                FROM
                    `api.daily_active_case` v
                INNER JOIN
                    `api.country` c ON (c.id = v.country_id)
                WHERE
                    date_field = (SELECT max(date_field) FROM `api.daily_active_case`)
                    AND c.alpha2_code = %s
            ''', [country])
        else:
            cursor.execute('''
                SELECT
                    SUM(total),
                    date_field
                FROM
                    `api.daily_active_case` v
                WHERE
                    date_field = (SELECT max(date_field) FROM `api.daily_active_case`)
            ''')

        row = cursor.fetchone()

    return row


def select_all_active_global():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                SUM(total),
                date_field
            FROM
                `api.daily_active_case` 
            WHERE
                date_field = (SELECT max(date_field) FROM `api.daily_active_case`)
        ''')

        row = cursor.fetchone()

    return row


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
