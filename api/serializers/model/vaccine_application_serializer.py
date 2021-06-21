from rest_flex_fields import FlexFieldsModelSerializer
from api.models import VaccineApplication


class VaccineApplicationSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = VaccineApplication
        exclude = [
            "enabled",
            "created_on",
            "updated_on"
        ]
        expandable_fields = {
            "country": "api.serializers.model.country_serializer.CountrySerializer",
            "vaccine": ("api.serializers.model.vaccine_serializer.VaccineSerializer", {'many': True})
        }
