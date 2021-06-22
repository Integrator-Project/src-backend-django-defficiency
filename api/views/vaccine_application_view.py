from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import VaccineApplication
from ..repositories import when_started_vaccination_by_country
from ..serializers import VaccineApplicationSerializer


class VaccineApplicationViewSet(FlexFieldsModelViewSet):
    queryset = VaccineApplication.objects.all()
    serializer_class = VaccineApplicationSerializer
    permit_list_expands = ['country', 'vaccine']

    @action(methods=['GET'],
            detail=False,
            url_path=r'started/(?P<alpha2_code>\D+)')
    def started_vaccination(self, request, *args, **kwargs):
        code = kwargs.get('alpha2_code')
        response = when_started_vaccination_by_country(code)

        response_dict = {
            'date': response[0].isoformat()
        }

        return Response(response_dict)
