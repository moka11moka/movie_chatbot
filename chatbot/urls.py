from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from chatbot import settings

urlpatterns = [

    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^assets/(?P<path>.*)$", serve, {"document_root": settings.ASSETS_ROOT}),
    path('api/', include(("api.urls.urls", "api"), namespace="api")),
    path('', include(("dashboard.urls", "dashboard"), namespace="dashboard"))
]
