from rest_framework import viewsets
from ..models import VaccineApplication
from ..serializers import VaccineApplicationSerializer


class VaccineApplicationViewSet(viewsets.ModelViewSet):
    queryset = VaccineApplication.objects.all()
    serializer_class = VaccineApplicationSerializer
