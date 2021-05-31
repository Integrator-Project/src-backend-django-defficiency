from rest_flex_fields import FlexFieldsModelSerializer
from ..models import DailyDeath


class DailyDeathSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyDeath
        fields = "__all__"
