from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from ..models import Vaccine


class VaccineSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Vaccine
        fields = "__all__"
