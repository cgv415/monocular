from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Noticia
# Create your views here.

#En desuso
#Vista para mostrar la pagina principal de noticias
def Noticias(request):
    inicio = 2
    fin = 5
    noticias = Noticia.objects.order_by('-fecha')[inicio:fin]
    return render_to_response('noticias/noticias.html',{'noticias':noticias,'inicio':inicio,'range':range(5,10)},context_instance=RequestContext(request))

def PageNoticias(request,offset):
    cod = int(offset)
    has_prev=False
    has_next=True
    ini = cod*5
    fin = ini+5
    sig = cod+1
    ant = cod-1
    noticias = Noticia.objects.order_by('-fecha')[ini:fin]
    count = Noticia.objects.all().count()
    if cod >0:
        has_prev = True
    if count < fin:
        has_next = False
    return render_to_response('noticias/page.html',{'noticias':noticias,'has_next':has_next,'sig':sig,'has_prev':has_prev,'sig':sig,'ant':ant,'cod':cod},context_instance=RequestContext(request))

#vista para ver una noticia por separado, en un post
def Post(request,offset):
    cod = int(offset)
    noticia = Noticia.objects.filter(id=cod)[0]
    return render_to_response('noticias/post.html',{'noticia':noticia},context_instance=RequestContext(request))
