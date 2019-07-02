from django.urls import path

from . import views

urlpatterns = [
    path('forecast/', views.forecast, name='forecast'),
    path('forecast/alert/', views.forecast_alert, name='forecast_alert'),
    path('comparison/', views.comparison, name='comparison'),
    path('comparison/alert/', views.comparison_alert, name='comparison_alert'),
    path('mapscreen/', views.mapscreen, name="mapscreen"),
    path('', views.index, name='index'),
]