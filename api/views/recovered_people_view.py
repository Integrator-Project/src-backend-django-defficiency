from rest_framework import viewsets
from ..models import RecoveredPeople
from ..serializers import RecoveredPeopleSerializer


class RecoveredPeopleViewSet(viewsets.ModelViewSet):
    queryset = RecoveredPeople.objects.all()
    serializer_class = RecoveredPeopleSerializer
