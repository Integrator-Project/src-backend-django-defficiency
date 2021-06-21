from rest_framework import viewsets
from ..models import AlternativeNameVaccine
from ..serializers import AlternativeNameVaccineSerializer


class AlternativeNameVaccineViewSet(viewsets.ModelViewSet):
    queryset = AlternativeNameVaccine.objects.all()
    serializer_class = AlternativeNameVaccineSerializer
