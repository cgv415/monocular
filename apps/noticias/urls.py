from django.conf.urls import url
#from .views import index, index2,inicio,RegistrarNoticia

urlpatterns = [
   #url(r'^$' , 'apps.inicio.views.index'),
   url(r'^$', 'apps.noticias.views.Noticias',name="noticias"),
   url(r'^page/(\d+)/$' , 'apps.noticias.views.PageNoticias',name="noticias"),
   url(r'^post/(\d+)/$', 'apps.noticias.views.Post', name="post"),
]