from toolbox.api.permissions.permissions import ExemptCheckPermission
from toolbox.api.generic import BaseCreateAPIView
from api.service.forms import ServiceForm
from api.service.serializers import ServiceItemSerializer


class ServiceRetrieveView(BaseCreateAPIView):
    #处理请求
    create_form = ServiceForm
    #序列化ServiceForm里面的内容
    serializer_class = ServiceItemSerializer
    #api有权限
    permission_classes = (ExemptCheckPermission, )
