from django.utils.datastructures import MultiValueDictKeyError
from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import CountrySerializer
from ..services import *


class CountryViewSet(FlexFieldsModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['GET'],
            detail=False,
            url_path='total-daily-data')
    def get_total_daily_data(self, request, *args, **kwargs):
        try:
            alpha2_code = request.query_params['country']
        except MultiValueDictKeyError:
            alpha2_code = None

        return Response(total_daily_data(alpha2_code))

    @action(methods=['GET'],
            detail=False,
            url_path=r'data-per-month/(?P<alpha2_code>\D+)')
    def get_data_per_month(self, request, *args, **kwargs):
        code = kwargs.get('alpha2_code')
        return Response(data_per_month(code))
