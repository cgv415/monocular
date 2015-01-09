from django.views.generic import CreateView,TemplateView,ListView
from .models import Autor
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

# Create your views here.
class ResgistrarAutor(CreateView):
    template_name='autores/registrarAutor.html'
    model = Autor
    fields=['nombre','pais','descripcion','foto']
    success_url = reverse_lazy('reportar_autor')
    
def ReportarAutor(request):
    autores = Autor.objects.all()
    return render_to_response('autores/reportarAutor.html',{'autores':autores})