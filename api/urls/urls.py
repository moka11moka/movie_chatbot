from django.urls import path, include


#从url来，http://localhost:8888/api/service/,再到api.service.urls
urlpatterns = [
    path('service/', include(('api.service.urls', 'service'), namespace='service')),
]