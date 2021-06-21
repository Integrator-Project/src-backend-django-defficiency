from rest_flex_fields import FlexFieldsModelSerializer
from api.models import AlternativeNameVaccine


class AlternativeNameVaccineSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = AlternativeNameVaccine
        exclude = [
            "enabled",
            "created_on",
            "updated_on"
        ]
        expandable_fields = {
            "vaccine": "api.serializers.vaccine_serializer.VaccineSerializer"
        }
