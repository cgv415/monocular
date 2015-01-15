from django.conf.urls import url
#from .views import index, index2,inicio,RegistrarNoticia

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$' , 'apps.portfolio.views.Portfolio',name="portfolio"),
]