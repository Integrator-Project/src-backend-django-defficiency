from api.repositories import *
from api.serializers import CountrySerializer, VaccineSerializer


def all_data_country(alpha2_code):
    c_value, c_date = select_total_confirmed(alpha2_code)
    a_value, a_date = select_total_active(alpha2_code)
    r_value, r_date = select_total_recovered(alpha2_code)
    d_value, d_date = select_total_death(alpha2_code)
    last_update, percentage_second, percentage_first, total, first, second = select_data_vaccination(alpha2_code)
    started = select_started_vaccination(alpha2_code)

    list_vaccines = [Vaccine(*x) for x in select_vaccines_applied(alpha2_code)]
    vaccines = VaccineSerializer(list_vaccines, many=True)

    try:
        country = CountrySerializer(get_country_by_alpha2(alpha2_code)).data
    except ObjectDoesNotExist:
        country = {
            'name': 'Earth',
            'population': world_population()[0]
        }

    return {
        'country': country,
        'vaccination': {
            'started': started[0],
            'last_update': last_update,
            'percentage_second_dose': percentage_second,
            'percentage_first_dose': percentage_first,
            'total_vaccination': total,
            'people_vaccinated': first,
            'people_fully_vaccinated': second,
            'vaccines': vaccines.data,
        },
        'daily': {
            'confirmed': {
                'value': c_value, 'last_update': c_date
            },
            'active': {
                'value': a_value, 'last_update': a_date
            },
            'recovered': {
                'value': r_value, 'last_update': r_date
            },
            'death': {
                'value': d_value, 'last_update': d_date
            }
        }
    }


def daily_data_per_month(alpha2_code, last_months):
    try:
        country = CountrySerializer(get_country_by_alpha2(alpha2_code)).data
    except ObjectDoesNotExist:
        country = {
            'name': 'Earth',
            'population': world_population()[0]
        }

    confirmed = select_total_confirmed_per_month(alpha2_code, last_months)
    active = select_total_active_per_month(alpha2_code, last_months)
    recovered = select_total_recovered_per_month(alpha2_code, last_months)
    death = select_total_death_per_month(alpha2_code, last_months)

    return {
        'country': country,
        'confirmed': confirmed,
        'active': active,
        'recovered': recovered,
        'death': death
    }
