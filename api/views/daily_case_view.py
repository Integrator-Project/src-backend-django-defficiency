from rest_framework import viewsets
from ..models import DailyCase
from ..serializers import DailyCaseSerializer


class DailyCaseViewSet(viewsets.ModelViewSet):
    queryset = DailyCase.objects.all()
    serializer_class = DailyCaseSerializer
