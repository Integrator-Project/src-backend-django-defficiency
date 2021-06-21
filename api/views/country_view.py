from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import CountrySerializer
from ..services import *


class CountryViewSet(FlexFieldsModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['GET'], detail=False)
    def test(self, request):
        # post_vaccine_application()
        # post_all_countries_data()
        # get_all_vaccine_application_by_country(1)
        # post_global_daily_death()
        # post_global_daily_case()
        # post_global_all()
        return Response(True)
