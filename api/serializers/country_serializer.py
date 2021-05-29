from rest_flex_fields import FlexFieldsModelSerializer
from ..models import Country


class CountrySerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Country
        exclude = [
            "enabled",
            "created_on",
            "updated_on",
            "numeric_code",
            "region",
            "sub_region",
            "native_name"
        ]
        expandable_fields = {
            "continent": "api.serializers.continent_serializer.ContinentSerializer"
        }
