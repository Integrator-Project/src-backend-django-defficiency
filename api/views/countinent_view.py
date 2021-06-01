from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from ..models import Continent
from ..serializers import ContinentSerializer, CountryVaccinationDataSerializer
from ..services import get_content_country_vaccination


class ContinentViewSet(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

    @action(methods=['GET'], detail=False)
    def test(self, request):
        response = get_content_country_vaccination()
        serialized = CountryVaccinationDataSerializer(many=True, instance=response)

        return Response(serialized.data)
