from rest_flex_fields import FlexFieldsModelSerializer
from api.models import DailyActiveCase


class DailyActiveCaseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyActiveCase
        fields = "__all__"
