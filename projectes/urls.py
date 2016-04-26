from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^alertas/$', views.alertas_menu, name='alertas_menu'),
    url(r'^alertas/(?P<tipo>[0-2]+)/$', views.tipus, name='tipo'),
    url(r'^setVisto/(?P<id_par>[0-9]+)/$', views.visto, name='visto'),
    url(r'^propuestas/$', views.propuestas_menu, name='propuestas_menu'),
    url(r'^propuestas/add$', views.formPropuesta, name='form_propuesta'),
    url(r'^propuestas/get/(?P<tipo>[1-3]+)/$', views.propuestas_tipo, name='propuestas_tipo'),
    url(r'^propuestas/estado/(?P<id>[0-9]+)/(?P<tipo>[1-3]+)/$', views.setTipoPropuesta, name='propuestas_tipo_propuesta'),
    url(r'^propuestas/(?P<id_par>[0-9]+)/$', views.generarProyecto, name='generarProyecto'),
    url(r'^proyectos/$', views.proyectos_menu, name='proyectos_menu'),
    url(r'^proyectos/proyecto/(?P<id_pro>[0-9]+)/$', views.proyecto, name='proyecto'),
    url(r'^proyectos/(?P<tipo>[0-9]+)/$', views.tipoProyecto, name='tipoProyecto'),
]
