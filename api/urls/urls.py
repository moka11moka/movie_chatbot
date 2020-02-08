from django.urls import path, include


urlpatterns = [
    path('service/', include(('api.service.urls', 'service'), namespace='service')),
]