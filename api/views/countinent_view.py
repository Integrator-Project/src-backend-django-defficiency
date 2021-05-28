from rest_framework import viewsets
from ..models import Continent
from ..serializers import ContinentSerializer


class ContinentViewSet(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
