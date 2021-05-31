from rest_flex_fields import FlexFieldsModelSerializer
from ..models import VaccineApplication


class VaccineApplicationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = VaccineApplication
        fields = "__all__"
