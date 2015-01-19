from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView
from django.core.mail.message import EmailMessage
from apps.noticias.models import Noticia
from .forms import Formulario
from .models import VideoInicial
from apps.servicios.models import Proyecto
# Create your views here.

#Vista principal de la pagina web
def inicio(request):
    #Creamos un objeto noticias, no hace falta tiparlo
    #Lo igualamos a todos los objetos noticias (se tipa automaticamente a lista de noticias)
    #Ordenamos las noticias por fecha y le damos la vuelta, para que la primera noticia sea la ultima creada
    noticias = Noticia.objects.order_by('-fecha')
    video = VideoInicial.objects.filter(activo = True).order_by('id').reverse()[0]
    producciones = Proyecto.objects.filter(portfolio = True).order_by('-id')

    return render_to_response('inicio/inicio.html',{'video':video,'noticias':noticias,'producciones':producciones},context_instance=RequestContext(request))

#vista para el contacto
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

#En desuso
def index(request):
    noticias = Noticia.objects.all()
    return render_to_response('inicio/index.html',{'noticias':noticias},context_instance=RequestContext(request))

#Buen ejemplo para listview (mostrar objetos de forma sencilla)
class index2(ListView):
    template_name='inicio/index2.html'
    model = Noticia
    context_object_name = 'noticias'
