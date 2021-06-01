from rest_flex_fields import FlexFieldsModelSerializer
from api.models import ActiveCase


class ActiveCaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ActiveCase
        fields = "__all__"
