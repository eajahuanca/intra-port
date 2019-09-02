from rest_framework import serializers
from .models import (
    TipoContenido,
    Contenido,
    MisionVision,
    Banner,
    EnlacesSistemas
)


class MisionVisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MisionVision
        fields = '__all__'


class TipoContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoContenido
        fields = '__all__'


class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class EnlacesSistemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnlacesSistemas
        fields = '__all__'

