from rest_flex_fields import FlexFieldsModelSerializer
from api.models import VaccineApplication


class VaccineApplicationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = VaccineApplication
        fields = "__all__"
