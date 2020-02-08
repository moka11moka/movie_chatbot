from django.urls import path
from dashboard import views


urlpatterns = [
    path('', views.home_view, name='home')
]