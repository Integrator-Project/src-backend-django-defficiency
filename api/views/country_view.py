from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Country
from ..serializers import CountrySerializer
from ..services import post_all_countries_data, get_all_countries_data


class CountryViewSet(FlexFieldsModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(methods=['GET'], detail=False)
    def test(self, request):
        # response = get_all_countries_data()
        # serializer = self.get_serializer_class()
        # test = serializer(response, many=True)

        return Response(True)
