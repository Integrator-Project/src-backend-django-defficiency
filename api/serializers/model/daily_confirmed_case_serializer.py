from rest_flex_fields import FlexFieldsModelSerializer
from api.models import DailyConfirmedCase


class DailyConfirmedCaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyConfirmedCase
        fields = "__all__"
