from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework.serializers import ModelSerializer

from api.models import Country


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
