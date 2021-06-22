from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.db import connection
from api.models import DailyRecoveredPeople
from api.requests.daily_request import DailyRequest


def select_total_recovered_per_month(alpha2_code, last_months):
    with connection.cursor() as cursor:
        if alpha2_code is not None:
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
                    AND date_field BETWEEN DATE_ADD(NOW(), INTERVAL %s MONTH) AND NOW() 
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
            ''', [alpha2_code, -int(last_months), alpha2_code])
        else:
            cursor.execute('''
                        SELECT
                            SUM(cc.total),
                            cc.date_field
                        FROM
                            `api.daily_recovered_people` cc
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
                                                    `api.daily_recovered_people` cc
                                                INNER JOIN
                                                    `api.country` c ON (cc.country_id = c.id) 
                                                GROUP BY 1, 2) as ultimo)
                         GROUP BY cc.date_field
                         ORDER BY date_field
            ''', [-int(last_months)])

        row = cursor.fetchall()

    return row


def select_total_recovered(country):
    with connection.cursor() as cursor:
        if country is not None:
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
        else:
            cursor.execute('''
                SELECT
                    SUM(total),
                    date_field
                FROM
                    `api.daily_recovered_people` v
                WHERE
                    date_field = (SELECT max(date_field) FROM `api.daily_recovered_people`)
            ''')

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
