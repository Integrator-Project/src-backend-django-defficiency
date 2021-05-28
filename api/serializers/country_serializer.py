from rest_flex_fields import FlexFieldsModelSerializer
from ..models import Country
from .continent_serializer import ContinentSerializer


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
            "continent": ContinentSerializer
        }
