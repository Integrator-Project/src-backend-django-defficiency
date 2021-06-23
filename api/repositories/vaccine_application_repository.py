from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from api.models import Country, VaccineApplication
from api.requests import CountryVaccinationDataRequest


def select_world_data():
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT
            pop, total, (total * 100 / pop) porcentagem 
        FROM  
            (SELECT
                SUM(total_vaccinations) AS total 
            FROM
                `api.vaccine_application` 
            WHERE
                date_field = (SELECT MAX(date_field) FROM `api.vaccine_application`)) temp, 
                (SELECT SUM(population) pop FROM `api.country`) temp2
        ''')

        row = cursor.fetchone()

    return row


def select_most_percentage_second(limit):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                c.alpha2_code,
                SUM(v.people_fully_vaccinated),
                SUM(v.people_fully_vaccinated) * 100 / c.population AS porcentagem
            FROM
                `api.vaccine_application` v
            INNER JOIN
                `api.country` c ON (c.id = v.country_id)
            WHERE
                date_field = (SELECT MAX(date_field) FROM `api.vaccine_application`)
            GROUP BY c.name, c.population
            ORDER BY 3 DESC
            LIMIT %s
        ''', [int(limit)])

        row = cursor.fetchall()

    return row


def select_most_percentage_first(limit):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                c.alpha2_code,
                SUM(v.people_vaccinated),
                SUM(v.people_vaccinated) * 100 / c.population AS porcentagem
            FROM
                `api.vaccine_application` v
            INNER JOIN
                `api.country` c ON (c.id = v.country_id)
            WHERE
                date_field = (SELECT MAX(date_field) FROM `api.vaccine_application`)
            GROUP BY c.name, c.population
            ORDER BY 3 DESC
            LIMIT %s
        ''', [int(limit)])

        row = cursor.fetchall()

    return row


def select_most_vaccinated(limit):
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT
                c.alpha2_code,
                SUM(total_vaccinations),
                SUM(total_vaccinations) * 100 / c.population
            FROM
                `api.vaccine_application` v
            INNER JOIN
                `api.country` c ON (c.id = v.country_id)
            WHERE
                date_field = (SELECT MAX(date_field) FROM `api.vaccine_application`)
            GROUP BY c.name, c.population
            ORDER BY 2 DESC
            LIMIT %s
        ''', [int(limit)])

        row = cursor.fetchall()

    return row


def select_vaccines_applied(alpha2_code):
    with connection.cursor() as cursor:
        if alpha2_code is not None:
            cursor.execute('''
                SELECT
                    DISTINCT v.id,
                    v.created_on,
                    v.updated_on,
                    v.enabled,
                    v.name,
                    v.type,
                    v.description,
                    v.producer,
                    v.CAS_number,
                    v.drug_bank,
                    v.UNII,
                    v.KEGG,
                    v.pub_chem_SID
                FROM
                    `api.vaccine_application_vaccine` vav
                INNER JOIN
                    `api.vaccine_application` va ON (vav.vaccineApplication_id = va.id)
                INNER JOIN
                    `api.country` c ON (va.country_id = c.id)
                INNER JOIN
                    `api.vaccine` v ON (v.id = vav.vaccine_id)
                WHERE
                    c.alpha2_code = %s
            ''', [alpha2_code])
        else:
            cursor.execute('''
                SELECT
                    DISTINCT v.* FROM `api.vaccine_application_vaccine` vav
                INNER JOIN
                    `api.vaccine_application` va ON (vav.vaccineApplication_id = va.id)
                INNER JOIN
                    `api.country` c ON (va.country_id = c.id)
                INNER JOIN
                    `api.vaccine` v ON (v.id = vav.vaccine_id)
            ''')

        row = cursor.fetchall()

    return row


def select_total_vaccination_per_month(alpha2_code, last_months):
    with connection.cursor() as cursor:
        cursor.execute('''
        SELECT
            va.total_vaccinations,
            va.people_vaccinated,
            va.people_fully_vaccinated,
            va.date_field
        FROM
            `api.vaccine_application` va
        INNER JOIN
            `api.country` c ON (va.country_id = c.id) 
        WHERE
            va.date_field BETWEEN DATE_ADD(NOW(), INTERVAL %s MONTH) AND NOW() 
            AND c.alpha2_code = %s
            AND date_field IN (
                SELECT
                    CONCAT(ano, '-', mes, '-', dia) 
                FROM (SELECT 
                        MONTH(va.date_field) as mes,
                        YEAR(va.date_field) as ano,
                        MAX(DAY(va.date_field)) as dia 
                    FROM 
                        `api.vaccine_application` va
                    INNER JOIN
                        `api.country` c ON (va.country_id = c.id) 
                    WHERE
                        c.alpha2_code = %s 
                    GROUP BY 1, 2) as ultimo)
                ORDER BY date_field
        ''', [-int(last_months), alpha2_code, alpha2_code])
        row = cursor.fetchall()

    return row


def select_all_by_country(alpha2_code):
    return VaccineApplication.objects.filter(country__alpha2_code=alpha2_code)


def select_data_vaccination(alpha2_code):
    with connection.cursor() as cursor:
        if alpha2_code is not None:
            cursor.execute('''
                SELECT
                    MAX(date_field) AS 'ULTIMA ATUALIZACAO',
                    SUM(v.people_fully_vaccinated) * 100 / c.population AS 'PORCENTAGEM SEGUNDA DOSE',
                    SUM(v.people_vaccinated) * 100 / c.population AS 'PORCENTAGEM PRIMEIRA DOSE',
                    SUM(total_vaccinations) AS 'TOTAL VACINACAO',
                    SUM(people_vaccinated) AS 'PRIMEIRA DOSE',
                    SUM(people_fully_vaccinated) AS 'SEGUNDA DOSE'
                FROM
                    `api.vaccine_application` v
                INNER JOIN
                    `api.country` c ON (c.id = v.country_id)
                WHERE
                    date_field = (SELECT MAX(date_field) FROM `api.vaccine_application`)
                    AND c.alpha2_code = %s
            ''', [alpha2_code])
        else:
            cursor.execute('''
                SELECT
                    MAX(date_field) AS 'ULTIMA ATUALIZACAO',
                    SUM(v.people_fully_vaccinated) * 100 / SUM(c.population) AS 'PORCENTAGEM SEGUNDA DOSE',
                    SUM(v.people_vaccinated) * 100 / SUM(c.population) AS 'PORCENTAGEM PRIMEIRA DOSE',
                    SUM(total_vaccinations) AS 'TOTAL VACINACAO',
                    SUM(people_vaccinated) AS 'PRIMEIRA DOSE',
                    SUM(people_fully_vaccinated) AS 'SEGUNDA DOSE'
                FROM
                    `api.vaccine_application` v
                INNER JOIN
                    `api.country` c ON (c.id = v.country_id)
                WHERE
                    date_field = (SELECT MAX(date_field) FROM `api.vaccine_application`)
            ''')

        row = cursor.fetchone()

    return row


def select_started_vaccination(alpha2_code):
    with connection.cursor() as cursor:
        if alpha2_code is not None:
            cursor.execute('''
                SELECT
                    MIN(date_field) AS 'INICIO VACINACAO' FROM `api.vaccine_application` v
                INNER JOIN
                    `api.country` c ON (c.id = v.country_id)
                WHERE
                    c.alpha2_code = %s
            ''', [alpha2_code])
        else:
            cursor.execute('''
                SELECT
                    MIN(date_field) AS 'INICIO VACINACAO'
                FROM
                    `api.vaccine_application` v
            ''')

        row = cursor.fetchone()

    return row


def save_vaccine_application(
        request: CountryVaccinationDataRequest,
        country: Country,
        vaccines: list):
    try:
        vaccine_application = VaccineApplication.objects.get(date_field=request.date, country=country)
        return False, vaccine_application
    except ObjectDoesNotExist:
        vaccine_application = VaccineApplication.createByRequest(request, country)
        vaccine_application.save()
        vaccine_application.addMultipleVaccines(vaccines)
        return True, vaccine_application
