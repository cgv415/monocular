from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Corto,Estado_Corto
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required()
def MiFicha(request):
    usuario = request.user
    cortos = Corto.objects.filter(cliente_id = usuario.id)
    return render_to_response('servicios/mificha.html',{'cortos':cortos},context_instance=RequestContext(request))

def Servicios(request):
    return render_to_response('servicios/servicios.html',context_instance=RequestContext(request))

def Produccion(request):
    return render_to_response('servicios/produccion.html',context_instance=RequestContext(request))

def Postproduccion(request):
    return render_to_response('servicios/postproduccion.html',context_instance=RequestContext(request))

def Publicidad(request):
    return render_to_response('servicios/publicidad.html',context_instance=RequestContext(request))

def Distribucion(request):
    cortos = Corto.objects.all().order_by('id').reverse()
    return render_to_response('servicios/distribucion.html',{'cortos':cortos},context_instance=RequestContext(request))

def Cortometraje(request,offset):
    cod = int(offset)
    corto = Corto.objects.filter(id=cod)[0]
    estados = Estado_Corto.objects.filter(corto_id=cod)
    return render_to_response('servicios/cortometraje.html',{'corto':corto,'estados':estados},context_instance=RequestContext(request))
