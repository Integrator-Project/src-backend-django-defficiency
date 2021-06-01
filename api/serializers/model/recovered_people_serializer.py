from rest_flex_fields import FlexFieldsModelSerializer
from api.models import RecoveredPeople


class RecoveredPeopleSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = RecoveredPeople
        fields = "__all__"
