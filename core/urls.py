
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.Home,name='home'),
    path('administrador/',views.Admin,name='admin'),
    path('administrador/admcomunidades/coordinadores/<int:id>/',views.ListaCoordinadores,name='coordinadores'),
    path('administrador/admcomunidades/agentes/<int:id>/',views.ListaAgentes,name='agentes'),
    path('administrador/admcomunidades/ministros/<int:id>/',views.ListaMinistros,name='ministros'),
    path('administrador/admcomunidades/eventos/<int:id>/',views.ListaEventosMes,name='eventos'),
    path('administrador/admcomunidades/solicitudes/',views.ListaSolicitudes,name='solicitudes'),
    path('administrador/admcomunidades/agregar/',views.Agregar,name='agregar'),
    path('administrador/admcomunidades/agregar-comunidad/',views.AgregarComunidad,name='agregar_comunidad'),
    path('comunidades/',views.Comunidades,name='comunidades'),
    path('comunidades/bodas',views.ComunidadesB,name='comunidadesb'),
    path('comunidades/comuniones',views.ComunidadesC,name='comunidadesc'),
    path('comunidades/bautizos/<int:id>/',views.Bautizos,name='bautizos'),
    path('comunidades/bodas/<int:id>/',views.Bodas,name='bodas'),
    path('comunidades/comuniones/<int:id>/',views.Comuniones,name='comuniones'),
    path('comunidades/admcomunidades/agregar-evento/',views.AgregarEvento,name='agregare'),
]