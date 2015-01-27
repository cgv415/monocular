from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Proyecto,Estado_Proyecto,Galeria,Festival,Publicidad
from apps.administracion.models import TextoDescriptivo,Cliente, VideoInicial
from django.contrib.auth.decorators import login_required

# Create your views here.
#Ponemos login_required cuando queremos que solo usuarios autentificados puedan acceder a la vista
@login_required()
#En esta vista lo que se hace es mostrar todos los objetos creados a nombre del usuario que accede
def MiFicha(request):
    usuario = request.user
    cliente = Cliente.objects.get(usuario_id= request.user)
    proyectos = Proyecto.objects.filter(cliente_id = usuario.id).order_by('-id')
    return render_to_response('servicios/mificha.html',{'proyectos':proyectos,'cliente':cliente},context_instance=RequestContext(request))

#Muestra todos los servicios que se prestan
def Servicios(request):
    return render_to_response('servicios/servicios.html',context_instance=RequestContext(request))

#Muestra todos los s de produccion que se han creado
def Produccion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'produccion')[0]
    proyectos = Proyecto.objects.filter(servicio__nombre='Produccion',activo=True).order_by('-id')
    video = VideoInicial.objects.filter(activo = True).filter(tipo='produccion').order_by('id').reverse()[0]
    return render_to_response('servicios/produccion.html',{'texto':texto,'proyectos':proyectos,'video':video},context_instance=RequestContext(request))

#Muestra todos los objetos de postproduccion que se han creado
def Postproduccion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'postproduccion')[0]
    return render_to_response('servicios/postproduccion.html',{'texto':texto},context_instance=RequestContext(request))

#Muestra todos los anuncios que se han creado
def PublicidadPage(request):
    imagenes = []
    videos = []
    def dividir():
            anuncio = Publicidad.objects.all().order_by('-id')
            for a in anuncio:
                if a.video == '':
                    imagenes.append(a)
                else:
                    videos.append(a)
    
    
    dividir()
    
    texto = TextoDescriptivo.objects.filter(tipo = 'publicidad')[0]
    return render_to_response('servicios/publicidad.html',{'texto':texto,'imagenes':imagenes,'videos':videos},context_instance=RequestContext(request))

#Muestra todos los proyectos de distribucion que se han creado
def Distribucion(request):
    texto = TextoDescriptivo.objects.filter(tipo = 'distribucion')[0]
    proyectos = Proyecto.objects.filter(servicio__nombre='Distribucion',activo = True).order_by('-id')
    return render_to_response('servicios/distribucion.html',{'texto':texto,'proyectos':proyectos},context_instance=RequestContext(request))

#Muestra un proyecto
def Ficha(request,offset):
    cod = int(offset)
    proyectoR = Proyecto.objects.filter(id=cod)[0]
    estados = Estado_Proyecto.objects.filter(proyecto_id=cod)
    palmares = True;
    if estados.count()==0:
        palmares=False
    galeria = Galeria.objects.filter(proyecto=proyectoR).order_by('-id')
    return render_to_response('servicios/proyecto.html',{'palmares':palmares,'proyecto':proyectoR,'estados':estados,'galeria':galeria},context_instance=RequestContext(request))

#Muestra un Festival
def FestivalView(request,offset):
    cod = int(offset)
    festival = Festival.objects.filter(id=cod)[0]
    proyectos = Estado_Proyecto.objects.filter(festival__id=cod)
    return render_to_response('servicios/festival.html',{'festival':festival,'proyectos':proyectos},context_instance=RequestContext(request))

#Muestra un anuncio
def Anuncio(request,offset):
    cod = int(offset)
    anuncio = Publicidad.objects.filter(id=cod)[0]
    return render_to_response('servicios/anuncio.html',{'anuncio':anuncio,},context_instance=RequestContext(request))
