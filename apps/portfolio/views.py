from django.shortcuts import render_to_response
from django.template.context import RequestContext
from apps.servicios.models import Proyecto

# Create your views here.
def Portfolio(request):
    produccion = Proyecto.objects.filter(servicio='produccion').order_by('-id')
    colaboracion = Proyecto.objects.filter(servicio='colaboracion').order_by('-id')
    return render_to_response('portfolio/portfolio.html',{'produccion':produccion,'colaboracion':colaboracion},context_instance=RequestContext(request))