from rest_flex_fields import FlexFieldsModelSerializer
from ..models import DailyCase


class DailyCaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyCase
        fields = "__all__"
