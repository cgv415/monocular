from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
def Portafolios(request):
    return render_to_response('portafolios/portafolios.html',context_instance=RequestContext(request))