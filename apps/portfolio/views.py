from django.shortcuts import render_to_response
from django.template.context import RequestContext

# Create your views here.
def Portfolio(request):
    return render_to_response('portfolio/portfolio.html',context_instance=RequestContext(request))