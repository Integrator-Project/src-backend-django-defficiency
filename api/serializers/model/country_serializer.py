from rest_flex_fields import FlexFieldsModelSerializer
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
        expandable_fields = {
            "translations": ("api.serializers.model.translation_country_serializer.TranslationsCountrySerializer",
                             {"many": True, "omit": ["country"]}),
            "alternative_names": ("api.serializers.model.alternative_name_country_serializer"
                                  ".AlternativeNameCountrySerializer",
                                  {"many": True, "omit": ["country"]})
        }
