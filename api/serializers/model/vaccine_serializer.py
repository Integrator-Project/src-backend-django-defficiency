from rest_flex_fields import FlexFieldsModelSerializer
from api.models import Vaccine


class VaccineSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Vaccine
        fields = "__all__"
