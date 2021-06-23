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
        expandable_fields = {
            "alternative_names": ("api.serializers.model.alternative_name_vaccine_serializer"
                                  ".AlternativeNameVaccineSerializer", {'many': True, "omit": ["vaccine"]})
        }
