from django.urls import path
from api.service import views


urlpatterns = [
    #1.定义路径地址，2,如果找到了views处理
    path('', views.ServiceRetrieveView.as_view(), name='post'),
]