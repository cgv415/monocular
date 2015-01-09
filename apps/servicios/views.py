from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Corto
# Create your views here.
def Servicios(request):
    return render_to_response('servicios/servicios.html',context_instance=RequestContext(request))

def Produccion(request):
    return render_to_response('servicios/produccion.html',context_instance=RequestContext(request))

def Postproduccion(request):
    return render_to_response('servicios/postproduccion.html',context_instance=RequestContext(request))

def Publicidad(request):
    return render_to_response('servicios/publicidad.html',context_instance=RequestContext(request))

def Distribucion(request):
    cortos = Corto.objects.all()
    return render_to_response('servicios/distribucion.html',{'cortos':cortos},context_instance=RequestContext(request))

def Cortometraje(request,offset):
    cod = int(offset)
    corto = Corto.objects.filter(id=cod)[0]
    return render_to_response('servicios/cortometraje.html',{'corto':corto},context_instance=RequestContext(request))
