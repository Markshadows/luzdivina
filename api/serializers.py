from core.models import Comunidad, Evento
from rest_framework import serializers

class ComunidadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields= ('id','nombre','ubicacion')

class EventoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'nombre', 'fecha', 'descripcion', 'comunidad', 'solicitud')
