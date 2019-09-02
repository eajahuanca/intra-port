from rest_framework import serializers
from .models import (
    TipoSoporte,
    EstadoSolicitud,
    Calificacion,
    Solicitud
)


class TipoSoporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSoporte
        fields = '__all__'


class EstadoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSolicitud
        fields = '__all__'


class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = '__all__'


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'

