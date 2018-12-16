from django.shortcuts import render
from rest_framework import generics
from .serializers import ComunidadSerializers, EventoSerializers
from core.models import Comunidad, Evento
# Create your views here.
class ComunidadLista(generics.ListCreateAPIView):
    queryset = Comunidad.objects.all()
    serializer_class= ComunidadSerializers

class EventoComunidad(generics.ListCreateAPIView):
     serializer_class = EventoSerializers
     def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        fkcomunidad = self.kwargs['comunidad']
        return Evento.objects.filter(comunidad=fkcomunidad)