from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import viewsets
from ..models import TranslationsCountry
from ..serializers import TranslationsCountrySerializer


class TranslationsCountryViewSet(FlexFieldsModelViewSet):
    queryset = TranslationsCountry.objects.all()
    serializer_class = TranslationsCountrySerializer
