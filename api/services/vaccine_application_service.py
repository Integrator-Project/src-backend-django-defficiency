from api.models import Vaccine, Country
from api.repositories import select_data_vaccination, select_started_vaccination, \
    select_total_vaccination_per_month, select_vaccines_applied, select_most_percentage_second, \
    select_most_percentage_first, select_most_vaccinated, select_world_data
from api.serializers import VaccineSerializer, CountrySerializer
from utils import MostType


def world_data():
    pop, total, percentage = select_world_data()

    return {
        'population': pop,
        'total_vaccinations': total,
        'percentage_vaccination': percentage
    }


def most(limit, type):
    list_json = list()
    type_enum = MostType(type)

    result = {
        MostType.MOST_VACCINATED: select_most_vaccinated(limit),
        MostType.MOST_PERCENTAGE_SECOND: select_most_percentage_second(limit),
        MostType.MOST_PERCENTAGE_FIRST: select_most_percentage_first(limit)
    }.get(type_enum)

    for alpha2_code, total, percentage in result:
        list_json.append({
            'country': CountrySerializer(Country.objects.get(alpha2_code=alpha2_code), expand=['translations']).data,
            'percentage': percentage,
            'total': total
        })

    return {
        'type': str(type_enum),
        'result': list_json
    }


def total_per_month(alpha2_code, last_months, cumulative):
    result = list(select_total_vaccination_per_month(alpha2_code, last_months))
    json_list = list()

    if not cumulative:
        inverted = result.copy()[::-1]
        result.clear()

        for previous, current in zip(inverted, inverted[1:]):
            p_total, p_vaccinated, p_fully, p_date = previous
            c_total, c_vaccinated, c_fully, c_date = current

            total_result = abs(p_total - c_total)
            vaccinated_result = abs(p_vaccinated - c_vaccinated)
            fully_result = abs(p_fully - c_fully)

            result.append((total_result, vaccinated_result, fully_result, p_date))

        result.reverse()

    for total, people, fully, date in result:
        json_list.append({
            'total_vaccination': total,
            'people_vaccinated': people,
            'people_fully_vaccinated': fully,
            'date_field': date
        })

    return json_list


def vaccine_application_data(alpha2_code):
    last_update, p_second, p_first, total = select_data_vaccination(alpha2_code)
    started = select_started_vaccination(alpha2_code)

    list_vaccines = [Vaccine(*x) for x in select_vaccines_applied(alpha2_code)]
    vaccines = VaccineSerializer(list_vaccines, many=True)

    return {
        'started': started[0],
        'last_update': last_update,
        'percentage_second_dose': p_second,
        'percentage_first_dose': p_first,
        'total_vaccination': total,
        'vaccines': vaccines.data,
    }
