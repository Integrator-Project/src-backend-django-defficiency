from rest_flex_fields import FlexFieldsModelSerializer
from api.models import AlternativeNameCountry


class AlternativeNameCountrySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = AlternativeNameCountry
        exclude = [
            "enabled",
            "created_on",
            "updated_on"
        ]
        expandable_fields = {
            "country": "api.serializers.country_serializer.CountrySerializer"
        }
