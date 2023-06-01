from django.urls import path
from .views import SensorListCreateAPIView, SensorRetrieveUpdateAPIView, MeasurementListCreateAPIView, \
     SensorDetailRetrieveUpdateAPIView

urlpatterns = [
    path('sensors/', SensorListCreateAPIView.as_view()),
    path('sensors/<pk>/', SensorRetrieveUpdateAPIView.as_view()),
    path('measurements/', MeasurementListCreateAPIView.as_view()),
    path('sensors/<pk>/', SensorDetailRetrieveUpdateAPIView.as_view())
]
