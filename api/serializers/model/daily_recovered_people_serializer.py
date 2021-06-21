from rest_flex_fields import FlexFieldsModelSerializer
from api.models import DailyRecoveredPeople


class DailyRecoveredPeopleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = DailyRecoveredPeople
        fields = "__all__"
