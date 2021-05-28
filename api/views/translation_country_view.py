from rest_framework import viewsets
from ..models import TranslationsCountry
from ..serializers import TranslationsCountrySerializer


class TranslationsCountryViewSet(viewsets.ModelViewSet):
    queryset = TranslationsCountry.objects.all()
    serializer_class = TranslationsCountrySerializer
