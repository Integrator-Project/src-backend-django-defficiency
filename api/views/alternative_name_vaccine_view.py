from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework import viewsets
from ..models import AlternativeNameVaccine
from ..serializers import AlternativeNameVaccineSerializer


class AlternativeNameVaccineViewSet(FlexFieldsModelViewSet):
    queryset = AlternativeNameVaccine.objects.all()
    serializer_class = AlternativeNameVaccineSerializer
