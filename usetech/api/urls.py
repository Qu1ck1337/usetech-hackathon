from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('auth/', views.authentication, name='auth'),
    path('service1/', views.service1, name='service1'),
    path('service2/', views.service2, name='service2'),
]
