from rest_framework import viewsets
from ..models import DailyConfirmedCase
from ..serializers import DailyConfirmedCaseSerializer


class DailyConfirmedCaseViewSet(viewsets.ModelViewSet):
    queryset = DailyConfirmedCase.objects.all()
    serializer_class = DailyConfirmedCaseSerializer
