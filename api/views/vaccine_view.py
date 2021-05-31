from rest_framework import viewsets
from ..models import Vaccine
from ..serializers import VaccineSerializer


class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
