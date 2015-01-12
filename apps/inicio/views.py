from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from django.core.mail.message import EmailMessage
from apps.noticias.models import Noticia
from .forms import Formulario
from .models import Vimeo
#55951136
#32423533
#116108307
# Create your views here.
def inicio(request):
    noticias = Noticia.objects.order_by('fecha').reverse()
    #vimeo = Vimeo.objects.filter(activo = True).reverse()[0]
    vimeo = Vimeo.objects.get_or_create(codigo='32423533')
    return render_to_response('inicio/inicio.html',{'vimeo':vimeo,'noticias':noticias},context_instance=RequestContext(request))

def contacto(request):
    exito=False
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():   
            mail = form.cleaned_data['mail']
            nombre = form.cleaned_data['nombre']
            asunto = 'Mensaje de contacto de' + ' ' + nombre+  ', (' + mail+')'
            mensaje = form.cleaned_data['mensaje'] +' de '+ mail
            #send_mail(asunto,mensaje,['carlosgarrido993@gmail.com'])
            email=EmailMessage(asunto,mensaje,to=['carlosgarrido993@gmail.com'])
            email.send()
            exito=True        
            return render_to_response('inicio/contacto.html',{'exito':exito},context_instance=RequestContext(request))
    else:
        form = Formulario()
    return render_to_response('inicio/contacto.html',{'form':form,'exito':exito},context_instance=RequestContext(request))


def index(request):
    noticias = Noticia.objects.all()
    return render_to_response('inicio/index.html',{'noticias':noticias},context_instance=RequestContext(request))


class index2(ListView):
    template_name='inicio/index2.html'
    model = Noticia
    context_object_name = 'noticias'
