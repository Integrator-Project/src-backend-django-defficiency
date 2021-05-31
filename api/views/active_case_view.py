from rest_framework import viewsets
from ..models import ActiveCase
from ..serializers import ActiveCaseSerializer


class ActiveCaseViewSet(viewsets.ModelViewSet):
    queryset = ActiveCase.objects.all()
    serializer_class = ActiveCaseSerializer
