from rest_flex_fields import FlexFieldsModelSerializer
from api.models import TranslationsCountry


class TranslationsCountrySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TranslationsCountry
        exclude = [
            "enabled",
            "created_on",
            "updated_on"
        ]
        expandable_fields = {
            "country": "api.serializers.country_serializer.CountrySerializer"
        }
