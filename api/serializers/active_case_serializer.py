from rest_flex_fields import FlexFieldsModelSerializer
from ..models import ActiveCase


class ActiveCaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ActiveCase
        fields = "__all__"
