from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.utils import timezone
from .forms import addPropuestaForm


def index(request):
    template = loader.get_template('projectes/index.html')
    return HttpResponse(template.render(request))

def alertas_menu(request):
	alertas = Alerta.objects.filter(llegit=0)
	context = {'alertas': alertas}
	template = loader.get_template('projectes/alertas_menu.html')
	return HttpResponse(template.render(context, request))

def propuestas_menu(request):
	propuestas = Propuesta.objects.all()
	context = {'propuestas': propuestas}
	template = loader.get_template('projectes/propuestas_menu.html')
	return HttpResponse(template.render(context, request))

def proyectos_menu(request):
	proyectos = Proyecto.objects.all()
	context = {'proyectos': proyectos}
	template = loader.get_template('projectes/proyectos_menu.html')
	return HttpResponse(template.render(context, request))

def tipus(request, tipo):
	if tipo == '2':
		titol = 'Todas las alertas'
		alertas = Alerta.objects.all()
	else:
		if tipo == '0':
			titol = 'Alertas pendientes' 
		else:
			titol = 'Alertas revisadas'
		alertas = Alerta.objects.filter(llegit=tipo)

	template = loader.get_template('projectes/alertas.html')
	context = {'alertas': alertas, 'titol': titol}
	return HttpResponse(template.render(context, request))

def tipoProyecto(request, tipo):
	if tipo == '0':
		proyectos = Proyecto.objects.all()
	else:
		proyectos = Proyecto.objects.filter(tipo=tipo)
	template = loader.get_template('projectes/objetivo_proyectos.html')
	context = {'proyectos': proyectos}
	return HttpResponse(template.render(context, request))

def visto(request, id_par):
	alerta = Alerta.objects.get(id=id_par)
	if alerta.llegit == 1:
		alerta.llegit = 0
	else:
		alerta.llegit = 1
	alerta.save()
	return HttpResponse(request)

def generarProyecto(request, id_par):
	propuesta = Propuesta.objects.get(id=id_par)
	proyecto = Proyecto(titol=propuesta.titol, descripcio=propuesta.descripcio, data=timezone.now(), presupuesto=propuesta.presupuesto)
	proyecto.save()
	propuesta.delete()
	return HttpResponse(request)

def formPropuesta(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = addPropuestaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			print form.cleaned_data['presupuesto']
			propuesta = Propuesta(
				titol=form.cleaned_data['titol'],
				descripcio=form.cleaned_data['descripcio'],
				data=form.cleaned_data['data'],
				presupuesto=int(form.cleaned_data['presupuesto']))
			propuesta.save()
			return HttpResponseRedirect('..')
    else:
        form = addPropuestaForm()	

    return render(request, 'projectes/form_propuestas.html', {'form': form})

def proyecto(request, id_pro):
	proyecto = Proyecto.objects.get(id=id_pro)
	context = {'projecte': proyecto}
	template = loader.get_template('projectes/proyecto.html')
	return HttpResponse(template.render(context, request))