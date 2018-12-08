from django.shortcuts import render
from django.http import Http404
from .models import Coordinador, AgentePastoral, MinistroComunion, Comunidad, Evento, Sacramento, Solicitud
from django.views import generic


# Create your views here.
lista= Comunidad.objects.all()
l_solicitudes=Solicitud.objects.all()

def Home(request):
    if request.POST:
        
        nombre= request.POST["nombre"]
        descripcion= request.POST["descripcion"]
        comunidad=request.POST["comunidad"]

        obj_com= Comunidad.objects.get(id=comunidad)
        solicitud= Solicitud(
            nombre=nombre,
            descripcion = descripcion,
            comunidad=obj_com
        )
        solicitud.save()
        return render(request,'core/index.html',
                              {'lista':lista, 'mensaje':'Solicitud Enviada'})
    return render(request,'core/index.html',
                              {'lista':lista})   

def Admin(request):
    return render(request,'core/administrador.html',{'lista':lista})

def ListaCoordinadores(request, id):
    lista2= Coordinador.objects.filter(comunidad=id)
    comunidadNombre = Comunidad.objects.get(pk=id)
    return render(request,'core/comunidad/lista_coordinador.html',
                              {'lista2':lista2,'lista':lista,'comunidad':comunidadNombre})

def ListaAgentes(request, id):
    lista3= AgentePastoral.objects.filter(comunidad=id)
    comunidadNombre = Comunidad.objects.get(pk=id)
    return render(request,'core/comunidad/lista_agente.html',{'lista3':lista3, 'lista':lista, 
    'comunidad':comunidadNombre})

def ListaMinistros(request, id):
    lista4= MinistroComunion.objects.filter(comunidad=id)
    comunidadNombre = Comunidad.objects.get(pk=id)
    return render(request,'core/comunidad/lista_ministro.html',{'lista4':lista4, 'lista':lista,
    'comunidad':comunidadNombre})

def ListaEventos(request, id):
    comunidadNombre = Comunidad.objects.get(pk=id)
    lista5= Evento.objects.filter(comunidad=id)
    return render(request,'core/comunidad/lista_evento.html',{'lista5':lista5, 'lista':lista,
    'comunidad':comunidadNombre})

def ListaEventosMes(request, id):
    comunidadNombre = Comunidad.objects.get(pk=id)
    lista5= Evento.objects.filter(comunidad=id)
    if request.POST:
        try:
             mes_elegido= request.POST["mes_elegido"]
             lista5= Evento.objects.filter(comunidad=id, fecha__month=mes_elegido)
        except Evento.DoesNotExist:
            raise Http404("Question does not exist")
        return render(request,'core/comunidad/lista_evento.html',{'lista5':lista5, 'lista':lista,
        'comunidad':comunidadNombre})
    return render(request,'core/comunidad/lista_evento.html',{'lista5':lista5, 'lista':lista,
    'comunidad':comunidadNombre})

def DetalleCoordinador(request, id):
    try:
        coordinador = Coordinador.objects.get(pk=id)
    except Coordinador.DoesNotExist:
        raise Http404("No se insertó el mes")
    return render(request, 'core/comunidad/coordinador_detail.html', {'coordinador': coordinador})

def Agregar(request):
    sacramentos= Sacramento.objects.all()
    if request.POST:
        
        nombre= request.POST["nombre"]
        appaterno=request.POST["appaterno"]
        edad=request.POST["edad"]
        sacramento=request.POST["sacramento"]
        comunidad=request.POST["comunidad"]

        obj_sacr= Sacramento.objects.get(id=sacramento)
        obj_com= Comunidad.objects.get(id=comunidad)
        agente= AgentePastoral(
            nombre=nombre,
            appaterno=appaterno,
            edad=int(edad),
            sacramento=obj_sacr,
            comunidad=obj_com
        )
        agente.save()
        return render(request,'core/comunidad/agregar.html',
                              {'sacramento':sacramentos,'lista':lista, 'mensaje':'Agente Guardado'})
    return render(request,'core/comunidad/agregar.html',
                              {'sacramento':sacramentos,'lista':lista})

def AgregarComunidad(request):
    if request.POST:
        
        nombre= request.POST["nombre"]
        ubicacion=request.POST["ubicacion"]

        comunidad= Comunidad(
            nombre=nombre,
            ubicacion=ubicacion,
        )
        comunidad.save()
        return render(request,'core/comunidad/agregar_comunidad.html',
                              {'lista':lista, 'mensaje':'Comunidad Guardada'})
    return render(request,'core/comunidad/agregar_comunidad.html',
                              {'lista':lista})

def AgregarEvento(request):
    sacramentos= Sacramento.objects.all()
    if request.POST:
        
        fecha= request.POST["fecha"]
        hora= request.POST["hora"]
        descripcion=request.POST["descripcion"]
        sacramento=request.POST["sacramento"]
        comunidad=request.POST["comunidad"]
        solicitud=request.POST["solicitud"]

        obj_sacr= Sacramento.objects.get(id=sacramento)
        obj_com= Comunidad.objects.get(id=comunidad)
        obj_sol= Solicitud.objects.get(id=solicitud)
        evento= Evento(
            nombre=obj_sacr,
            fecha=fecha + ' '+ hora+':00',
            descripcion=descripcion,
            comunidad=obj_com,
            solicitud=obj_sol
        )
        obj_sol.estado = 'Aceptada'
        obj_sol.save()
        evento.save()

        return render(request,'core/comunidad/agregar_evento.html',
                              {'solicitudes':l_solicitudes,'sacramento':sacramentos,'lista':lista, 'mensaje':'Evento Guardado'})
    return render(request,'core/comunidad/agregar_evento.html',
                              {'solicitudes':l_solicitudes,'sacramento':sacramentos,'lista':lista})   

def Comunidades(request):
    return render(request,'core/publico/comunidades.html',{'lista':lista})

def ComunidadesB(request):
    return render(request,'core/publico/comunidadesb.html',{'lista':lista})

def ComunidadesC(request):
    return render(request,'core/publico/comunidadesc.html',{'lista':lista})

def Bautizos(request, id):
    comunidad = Comunidad.objects.get(pk=id)
    eventos= Evento.objects.filter(comunidad=id, nombre=1)
    return render(request,'core/publico/bautizos.html',{'comunidad':comunidad, 'eventos':eventos})

def Bodas(request, id):
    comunidad = Comunidad.objects.get(pk=id)
    eventos= Evento.objects.filter(comunidad=id, nombre=3)
    return render(request,'core/publico/bodas.html',{'comunidad':comunidad, 'eventos':eventos})

def Comuniones(request, id):
    comunidad = Comunidad.objects.get(pk=id)
    eventos= Evento.objects.filter(comunidad=id, nombre=2)
    return render(request,'core/publico/comuniones.html',{'comunidad':comunidad, 'eventos':eventos})

def ListaSolicitudes(request):
    return render(request,'core/comunidad/solicitudes.html',{'lista':lista, 'solicitudes':l_solicitudes})
   