from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Noticia
# Create your views here.
def Noticias(request):
    noticias = Noticia.objects.order_by('fecha').reverse()
    return render_to_response('noticias/noticias.html',{'noticias':noticias},context_instance=RequestContext(request))

def Post(request,offset):
    cod = int(offset)
    noticia = Noticia.objects.filter(id=cod)[0]
    return render_to_response('noticias/post.html',{'noticia':noticia},context_instance=RequestContext(request))
