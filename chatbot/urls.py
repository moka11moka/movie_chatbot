from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from chatbot import settings

#打开localhost:8888的入口文件

urlpatterns = [

    # 图片,组件
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^assets/(?P<path>.*)$", serve, {"document_root": settings.ASSETS_ROOT}),

    # api端口 会去找api.urls.urls中的文件
    path('api/', include(("api.urls.urls", "api"), namespace="api")),
    # 网页的路径地址
    path('', include(("dashboard.urls", "dashboard"), namespace="dashboard"))
]
