# from django.conf.urls import url
from django.urls import path

from . import views


urlpatterns = [
    path('', views.sms_response, name='sms'),
    path('weather', views.get_weather, name='weather')
]
