from django.urls import path
from api.service import views


urlpatterns = [
    path('', views.ServiceRetrieveView.as_view(), name='post'),
]