from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Proyecto,Estado_Corto,Galeria,Festival,Publicidad
from apps.administracion.models import TextoDescriptivo
from django.contrib.auth.decorators import login_required
# Create your views here.

#Ponemos login_required cuando queremos que solo usuarios autentificados puedan acceder a la vista
@login_required()
#En esta vista lo que se hace es mostrar todos los objetos creados a nombre del usuario que accede
def MiFicha(request):
    usuario = request.user
    proyectos = Proyecto.objects.filter(cliente_id = usuario.id).order_by('-id')
    return render_to_response('servicios/mificha.html',{'proyectos':proyectos},context_instance=RequestContext(request))

#Muestra todos los servicios que se prestan
def Servicios(request):
    return render_to_response('servicios/servicios.html',context_instance=RequestContext(request))

#Muestra todos los s de produccion que se han creado
def Produccion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'produccion')[0]
    proyectos = Proyecto.objects.filter(servicio__nombre='Produccion').order_by('-id')
    return render_to_response('servicios/produccion.html',{'texto':texto,'proyectos':proyectos},context_instance=RequestContext(request))

#Muestra todos los objetos de postproduccion que se han creado
def Postproduccion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'postproduccion')[0]
    return render_to_response('servicios/postproduccion.html',{'texto':texto},context_instance=RequestContext(request))

#Muestra todos los anuncios que se han creado
def PublicidadPage(request):
    publicidad = Publicidad.objects.all().order_by('-id')
    texto = TextoDescriptivo.objects.filter(tipo = 'publicidad')[0]
    return render_to_response('servicios/publicidad.html',{'texto':texto,'publicidad':publicidad},context_instance=RequestContext(request))

#Muestra todos los proyectos de distribucion que se han creado
def Distribucion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'distribucion')[0]
    proyectos = Proyecto.objects.filter(servicio__nombre='Distribucion').order_by('-id')
    return render_to_response('servicios/distribucion.html',{'texto':texto,'proyectos':proyectos},context_instance=RequestContext(request))

#Muestra un proyecto
def Ficha(request,offset):
    cod = int(offset)
    proyectoR = Proyecto.objects.filter(id=cod)[0]
    estados = Estado_Corto.objects.filter(corto_id=cod)
    galeria = Galeria.objects.filter(proyecto=proyectoR).order_by('-id')
    return render_to_response('servicios/proyecto.html',{'proyecto':proyectoR,'estados':estados,'galeria':galeria},context_instance=RequestContext(request))

#Muestra un Festival
def FestivalView(request,offset):
    cod = int(offset)
    festival = Festival.objects.filter(id=cod)[0]
    proyectos = Estado_Corto.objects.filter(festival__id=cod)
    return render_to_response('servicios/festival.html',{'festival':festival,'proyectos':proyectos},context_instance=RequestContext(request))

#Muestra un anuncio
def Anuncio(request,offset):
    cod = int(offset)
    anuncio = Publicidad.objects.filter(id=cod)[0]
    return render_to_response('servicios/anuncio.html',{'anuncio':anuncio,},context_instance=RequestContext(request))
