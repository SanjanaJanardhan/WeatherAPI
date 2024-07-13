from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('forecast/<str:city>/', views.forecast_weather, name='forecast_weather'),
    path('historical/<str:city>/<str:date>/', views.historical_weather, name='historical_weather'),
]
