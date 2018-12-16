
from django.conf.urls import url
from .views import ComunidadDetalle,ComunidadLista,EventoComunidad

urlpatterns = [
    url('comunidad_lista/',ComunidadLista.as_view()),
    url('^comunidad_evento/(?P<comunidad>.+)/$', EventoComunidad.as_view()),
]