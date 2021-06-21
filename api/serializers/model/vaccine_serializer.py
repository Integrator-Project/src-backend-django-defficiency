from rest_flex_fields import FlexFieldsModelSerializer
from api.models import Vaccine


class VaccineSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Vaccine
        exclude = [
            "enabled",
            "created_on",
            "updated_on"
        ]
