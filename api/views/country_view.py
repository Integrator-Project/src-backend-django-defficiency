from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from ..serializers import CountrySerializer
from ..services import *


class CountryViewSet(FlexFieldsModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    # @action(methods=['GET'],
    #         detail=False,
    #         url_path=r'started-vaccination/<str:alpha2_code>')
    # def started_vaccination(self, request, *args, **kwargs):
    #     params = request.query_params
    #     print(params)
    #     return Response(True)
