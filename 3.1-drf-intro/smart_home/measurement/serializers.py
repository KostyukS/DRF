from rest_framework import serializers
from .models import Measurement, Sensor


# TODO: опишите необходимые сериализаторы


class MeasurementSerializer(serializers.ModelSerializer):
    """Сериализатор для записи данных в модель Measurement"""
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']


class MeasurementSerializer1(serializers.ModelSerializer):
    """Сериализатор для чтения данных из модели Measurement"""
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения/записи в модель Sensor"""
    class Meta:
        model = Sensor
        fields = ['id', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для чтения данных из моделей Sensor и Measurement"""
    measurements = MeasurementSerializer1(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'description', 'measurements']
