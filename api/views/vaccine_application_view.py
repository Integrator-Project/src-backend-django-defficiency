from rest_flex_fields import FlexFieldsModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import VaccineApplication
from ..serializers import VaccineApplicationSerializer
from ..services import get_all_vaccine_application_by_country


class VaccineApplicationViewSet(FlexFieldsModelViewSet):
    queryset = VaccineApplication.objects.all()
    serializer_class = VaccineApplicationSerializer
    permit_list_expands = ['country', 'vaccine']

    # @action(methods=['GET'],
    #         detail=False,
    #         url_path=r'get-all-by-country')
    # def get_all_by_country(self, request):
    #     all_application = get_all_vaccine_application_by_country(1)
    #     serializer = VaccineApplicationSerializer(all_application, many=True)
    #     return Response(serializer.data)
