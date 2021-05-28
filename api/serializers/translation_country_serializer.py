from rest_flex_fields import FlexFieldsModelSerializer
from ..models import TranslationsCountry


class TranslationsCountrySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = TranslationsCountry
        fields = "__all__"
