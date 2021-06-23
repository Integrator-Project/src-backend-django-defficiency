from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import viewsets
from ..models import AlternativeNameCountry
from ..serializers import AlternativeNameCountrySerializer


class AlternativeNameCountryViewSet(FlexFieldsModelViewSet):
    queryset = AlternativeNameCountry.objects.all()
    serializer_class = AlternativeNameCountrySerializer
