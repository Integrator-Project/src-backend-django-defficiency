from rest_framework import viewsets
from ..models import DailyRecoveredPeople
from ..serializers import DailyRecoveredPeopleSerializer


class DailyRecoveredPeopleViewSet(viewsets.ModelViewSet):
    queryset = DailyRecoveredPeople.objects.all()
    serializer_class = DailyRecoveredPeopleSerializer
