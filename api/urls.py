
from django.conf.urls import url
from .views import ComunidadDetalle,ComunidadLista

urlpatterns = [
    url('comunidad_lista/',ComunidadLista.as_view()),
    url(r'^comunidad_detalle/(?P<pk>[0-9]+)/$',ComunidadDetalle.as_view()),
]