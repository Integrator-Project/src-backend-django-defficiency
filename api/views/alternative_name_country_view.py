from rest_framework import viewsets
from ..models import AlternativeNameCountry
from ..serializers import AlternativeNameCountrySerializer


class AlternativeNameCountryViewSet(viewsets.ModelViewSet):
    queryset = AlternativeNameCountry.objects.all()
    serializer_class = AlternativeNameCountrySerializer
