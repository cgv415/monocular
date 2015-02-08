from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail.message import EmailMessage
from apps.noticias.models import Noticia
from .forms import Formulario
from apps.administracion.models import VideoInicial,Informacion
from apps.servicios.models import Proyecto
# Create your views here.

#Vista principal de la pagina web
def inicio(request):
    #Creamos un objeto noticias, no hace falta tiparlo
    #Lo igualamos a todos los objetos noticias (se tipa automaticamente a lista de noticias)
    #Ordenamos las noticias por fecha y le damos la vuelta, para que la primera noticia sea la ultima creada
    noticias = Noticia.objects.filter(activo=True).order_by('-fecha','-id')
    video = VideoInicial.objects.filter(activo = True).filter(tipo='inicio').order_by('id').reverse()[0]
    producciones = Proyecto.objects.filter(portfolio = True,activo=True).order_by('-id')
    return render_to_response('inicio/inicio.html',{'video':video,'noticias':noticias,'producciones':producciones},context_instance=RequestContext(request))

#Vista para el contacto
def contacto(request):
    exito=False
    informacion = Informacion.objects.all()[0]
    if request.method == 'POST':
        form = Formulario(request.POST)
        if form.is_valid():   
            mail = form.cleaned_data['mail']
            nombre = form.cleaned_data['nombre']
            telefono = form.cleaned_data['telefono']
            tlfn = str(telefono)
            asunto = 'Mensaje de contacto de' + ' ' + nombre+  ', (' + mail+')'
            mensaje = form.cleaned_data['mensaje'] +'\n De: '+ mail + '\n telefono: ' + tlfn
            #send_mail(asunto,mensaje,['carlosgarrido993@gmail.com'])
            email=EmailMessage(asunto,mensaje,to=['carlosgarrido993@gmail.com'])
            email.send()
            emailCopy=EmailMessage(asunto,mensaje,to=[mail])
            emailCopy.send()
            exito=True        
            return render_to_response('inicio/contacto.html',{'informacion':informacion,'exito':exito},context_instance=RequestContext(request))
    else:
        form = Formulario()
    return render_to_response('inicio/contacto.html',{'informacion':informacion,'form':form,'exito':exito},context_instance=RequestContext(request))

def gallery(request):
    return render_to_response('inicio/image-gallery.html',context_instance=RequestContext(request))
