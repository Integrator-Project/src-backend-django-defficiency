from rest_framework import viewsets
from ..models import DailyActiveCase
from ..serializers import DailyActiveCaseSerializer


class DailyActiveCaseViewSet(viewsets.ModelViewSet):
    queryset = DailyActiveCase.objects.all()
    serializer_class = DailyActiveCaseSerializer
