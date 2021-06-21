from rest_flex_fields import FlexFieldsModelSerializer
from api.models import DailyDeath


class DailyDeathSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyDeath
        fields = "__all__"
