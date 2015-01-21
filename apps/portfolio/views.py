from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.servicios.models import Proyecto

# Create your views here.
def Portfolio(request):
    proyectos = Proyecto.objects.filter(servicio__nombre='Produccion').order_by('-id')
    colaboraciones = Proyecto.objects.filter(servicio__nombre='Colaboracion').order_by('-id')
    return render_to_response('portfolio/portfolio.html',{'proyectos':proyectos,'colaboraciones':colaboraciones},context_instance=RequestContext(request))