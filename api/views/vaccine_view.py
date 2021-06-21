from rest_flex_fields import FlexFieldsModelViewSet
from ..models import Vaccine
from ..serializers import VaccineSerializer


class VaccineViewSet(FlexFieldsModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
