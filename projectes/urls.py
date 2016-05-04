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
    url(r'^proyectos/(?P<tipo>[0-9]+)/$', views.tipoProyecto, name='tipoProyecto'),
    url(r'^objetivos/$', views.generarOjetivos, name='generarOjetivos'),
    url(r'^objetivos/add$', views.formObjetivo, name='formObjetivo'),
    url(r'^objetivo/eliminar/(?P<id>[0-9]+)/$', views.eliminarObj, name='eliminarObj'),
    url(r'^objetivo/mod/(?P<id>[0-9]+)/$', views.modificarObj, name='modificarObj'),
    url(r'^principios/$', views.generarPrincipios, name='generarPrincipios'),
    url(r'^principio/mod/(?P<id>[0-9]+)/$', views.modificarPrincipio, name='modificarPrincipio'),
    url(r'^principio/eliminar/(?P<id>[0-9]+)/$', views.eliminarPrin, name='eliminarPrin'),
    url(r'^principio/add$', views.formPrincipio, name='formPrincipio'),
    url(r'^proyectos/proyecto/individual/(?P<id>[0-9]+)/$', views.selectProyecto, name='selectProyecto'),
    url(r'^presupuestos/$', views.presupuestos, name='presupuestos'),
]
