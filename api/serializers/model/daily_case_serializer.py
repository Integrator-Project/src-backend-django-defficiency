from rest_flex_fields import FlexFieldsModelSerializer
from api.models import DailyCase


class DailyCaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyCase
        fields = "__all__"
