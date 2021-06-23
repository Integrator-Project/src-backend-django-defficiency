import distutils
from distutils.util import strtobool

from django.utils.datastructures import MultiValueDictKeyError
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import CountrySerializer
from ..services import *


class CountryViewSet(FlexFieldsModelViewSet):
    permit_list_expands = ['translations', 'alternative_names']
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['GET'],
            detail=False,
            url_path='test')
    def test(self, request):
        post_vaccine_application()
        post_global_daily_death()
        post_global_daily_case()
        post_global_all()
        return Response(True)

    @action(methods=['GET'],
            detail=False,
            url_path='all-data')
    def get_all_data(self, request, *args, **kwargs):
        try:
            response = all_data_country(request.query_params['country'])
        except MultiValueDictKeyError:
            response = all_data_country(None)

        return Response(response)

    @action(methods=['GET'],
            detail=False,
            url_path=r'daily-data-per-month')
    def get_data_per_month(self, request, *args, **kwargs):
        try:
            alpha2_code = request.query_params['country']
        except MultiValueDictKeyError:
            alpha2_code = None

        try:
            cumulative = bool(strtobool(request.query_params['cumulative']))
        except MultiValueDictKeyError:
            cumulative = True

        try:
            last_months = int(request.query_params['last-months'])
            last_months -= 1 if cumulative else 0
        except MultiValueDictKeyError:
            last_months = 6

        return Response(daily_data_per_month(alpha2_code, last_months, cumulative))
