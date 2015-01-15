from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Corto,Estado_Corto
from apps.administracion.models import TextoDescriptivo
from django.contrib.auth.decorators import login_required
# Create your views here.
#Ponemos login_required cuando queremos que solo usuarios autentificados puedan acceder a la vista
@login_required()
#En esta vista lo que se hace es mostrar todos los objetos creados a nombre del usuario que accede
def MiFicha(request):
    usuario = request.user
    cortos = Corto.objects.filter(cliente_id = usuario.id).order_by('-id')
    return render_to_response('servicios/mificha.html',{'cortos':cortos},context_instance=RequestContext(request))

#Muestra todos los servicios que se prestan
def Servicios(request):
    return render_to_response('servicios/servicios.html',context_instance=RequestContext(request))

#Muestra todos los objetos de produccion que se han creado
def Produccion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'produccion')[0]
    return render_to_response('servicios/produccion.html',{'texto':texto},context_instance=RequestContext(request))

#Muestra todos los objetos de postproduccion que se han creado
def Postproduccion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'postproduccion')[0]
    return render_to_response('servicios/postproduccion.html',{'texto':texto},context_instance=RequestContext(request))

#Muestra todos los objetos de publicidad que se han creado
def Publicidad(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'publicidad')[0]
    return render_to_response('servicios/publicidad.html',{'texto':texto},context_instance=RequestContext(request))

#Muestra todos los objetos de distribucion que se han creado
def Distribucion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'distribucion')[0]
    cortos = Corto.objects.all().order_by('id').reverse()
    return render_to_response('servicios/distribucion.html',{'texto':texto,'cortos':cortos},context_instance=RequestContext(request))

#Muestra un cortometraje 
def Cortometraje(request,offset):
    cod = int(offset)
    corto = Corto.objects.filter(id=cod)[0]
    estados = Estado_Corto.objects.filter(corto_id=cod)
    return render_to_response('servicios/cortometraje.html',{'corto':corto,'estados':estados},context_instance=RequestContext(request))
