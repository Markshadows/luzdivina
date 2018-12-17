from core.models import Comunidad, Sacramento, Evento
from rest_framework import serializers

class SacramentoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Sacramento
        fields = ('id','nombre')

class ComunidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields= ('id','nombre','ubicacion', 'img')

class EventoSerializers(serializers.ModelSerializer):
    nombre = SacramentoSerializers(required=True)
    comunidad = ComunidadSerializers(required=True)
    class Meta:
        model = Evento
        fields = ('id', 'nombre', 'fecha', 'descripcion', 'comunidad', 'solicitud')
