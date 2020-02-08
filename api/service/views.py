from toolbox.api.permissions.permissions import ExemptCheckPermission
from toolbox.api.generic import BaseCreateAPIView
from api.service.forms import ServiceForm
from api.service.serializers import ServiceItemSerializer


class ServiceRetrieveView(BaseCreateAPIView):
    create_form = ServiceForm
    serializer_class = ServiceItemSerializer
    permission_classes = (ExemptCheckPermission, )
