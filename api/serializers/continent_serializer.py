from rest_flex_fields import FlexFieldsModelSerializer
from ..models import Continent


class ContinentSerializer(FlexFieldsModelSerializer):

    class Meta:
        model = Continent
        exclude = [
            "enabled",
            "created_on",
            "updated_on"
        ]
        expandable_fields = {
            "countries": ("api.serializers.country_serializer.CountrySerializer", {
                "many": True,
                "omit": ["continent"]
            })
        }
