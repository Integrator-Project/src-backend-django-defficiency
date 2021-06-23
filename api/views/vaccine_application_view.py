from distutils.util import strtobool

from django.utils.datastructures import MultiValueDictKeyError
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from utils import MostType
from ..models import VaccineApplication
from ..repositories import select_all_by_country
from ..serializers import VaccineApplicationSerializer
from ..services import vaccine_application_data, total_per_month, most, world_data


class VaccineApplicationViewSet(FlexFieldsModelViewSet):
    queryset = VaccineApplication.objects.all()
    serializer_class = VaccineApplicationSerializer
    permit_list_expands = ['country', 'vaccine', 'translations']

    # @action(methods=['GET'],
    #         detail=False,
    #         url_path=r'all/(?P<alpha2_code>\D+)')
    # def get_all_by_country(self, request, *args, **kwargs):
    #     code = kwargs.get('alpha2_code')
    #     serializer = VaccineApplicationSerializer(
    #         select_all_by_country(code),
    #         omit=['country'],
    #         expand=['vaccine'],
    #         many=True)
    #
    #     return Response(serializer.data)

    # @action(methods=['GET'],
    #         detail=False,
    #         url_path=r'data')
    # def get_vaccination_data(self, request, *args, **kwargs):
    #     try:
    #         alpha2_code = request.query_params['country']
    #     except MultiValueDictKeyError:
    #         alpha2_code = None
    #
    #     return Response(vaccine_application_data(alpha2_code))

    @action(methods=['GET'],
            detail=False,
            url_path=r'total-per-month/(?P<alpha2_code>\D+)')
    def get_total_vaccination_month(self, request, *args, **kwargs):
        try:
            cumulative = bool(strtobool(request.query_params['cumulative']))
        except MultiValueDictKeyError:
            cumulative = True

        try:
            last_months = int(request.query_params['last-months'])
            last_months -= 1 if cumulative else 0
        except MultiValueDictKeyError:
            last_months = 20

        code = kwargs.get('alpha2_code')
        return Response(total_per_month(code, last_months, cumulative))

    @action(methods=['GET'],
            detail=False,
            url_path='most')
    def get_most_vaccinated(self, request, *args, **kwargs):
        try:
            limit = request.query_params['limit']
            most_type = request.query_params['type']
        except MultiValueDictKeyError:
            limit = 250
            most_type = MostType.MOST_VACCINATED

        return Response(most(limit, most_type))

