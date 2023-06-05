from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView, \
    RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorSerializer
from rest_framework.response import Response


# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

class SensorListCreateAPIView(ListCreateAPIView):
    """Класс для получения датчиков из модели Sensor"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """Класс для создания (обновления) датчиков в модели Sensor"""
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementListCreateAPIView(ListCreateAPIView):
    """Класс для добавления измерения в модель Measurement"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorDetailRetrieveUpdateAPIView(RetrieveAPIView):
    """Класс для получения информации по датчику"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
