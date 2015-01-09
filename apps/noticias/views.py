from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Noticia
from apps.base.models import Menu
# Create your views here.
def Noticias(request):
    noticias = Noticia.objects.order_by('fecha').reverse()
    menus = Menu.objects.all()
    return render_to_response('noticias/noticias.html',{'noticias':noticias,'menus':menus},context_instance=RequestContext(request))
