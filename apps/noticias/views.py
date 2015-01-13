from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Noticia
# Create your views here.

#Vista para mostrar la pagina principal de noticias
def Noticias(request):
    noticias = Noticia.objects.order_by('fecha').reverse()
    return render_to_response('noticias/noticias.html',{'noticias':noticias},context_instance=RequestContext(request))

#vista para ver una noticia por separado, en un post
def Post(request,offset):
    cod = int(offset)
    noticia = Noticia.objects.filter(id=cod)[0]
    return render_to_response('noticias/post.html',{'noticia':noticia},context_instance=RequestContext(request))
