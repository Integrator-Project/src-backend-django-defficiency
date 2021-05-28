from rest_framework import viewsets
from ..models import DailyDeath
from ..serializers import DailyDeathSerializer


class DailyDeathViewSet(viewsets.ModelViewSet):
    queryset = DailyDeath.objects.all()
    serializer_class = DailyDeathSerializer
