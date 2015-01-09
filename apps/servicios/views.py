from django.shortcuts import render_to_response
from django.template import RequestContext
from apps.base.models import Menu
from .models import Corto
# Create your views here.
def Servicios(request):
    menus = Menu.objects.all()
    return render_to_response('servicios/servicios.html',{'menus':menus},context_instance=RequestContext(request))

def Produccion(request):
    menus = Menu.objects.all()
    return render_to_response('servicios/produccion.html',{'menus':menus},context_instance=RequestContext(request))

def Postproduccion(request):
    menus = Menu.objects.all()
    return render_to_response('servicios/postproduccion.html',{'menus':menus},context_instance=RequestContext(request))

def Publicidad(request):
    menus = Menu.objects.all()
    return render_to_response('servicios/publicidad.html',{'menus':menus},context_instance=RequestContext(request))

def Distribucion(request):
    menus = Menu.objects.all()
    cortos = Corto.objects.all()
    return render_to_response('servicios/distribucion.html',{'menus':menus,'cortos':cortos},context_instance=RequestContext(request))

def Cortometraje(request,offset):
    menus = Menu.objects.all()
    cod = int(offset)
    corto = Corto.objects.filter(id=cod)[0]
    return render_to_response('servicios/cortometraje.html',{'menus':menus,'corto':corto},context_instance=RequestContext(request))
