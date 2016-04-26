from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.utils import timezone
from .forms import addPropuestaForm
from django.db.models import Q


def index(request):
    template = loader.get_template('projectes/index.html')
    return HttpResponse(template.render(request))

def alertas_menu(request):
	alertas = Alerta.objects.filter(llegit=0)
	context = {'alertas': alertas}
	template = loader.get_template('projectes/alertas_menu.html')
	return HttpResponse(template.render(context, request))

def propuestas_tipo(request, tipo):
	propuestas = Propuesta.objects.filter(estado = tipo)
	context = {'propuestas': propuestas}
	template = loader.get_template('projectes/propuestas_menu.html')
	return HttpResponse(template.render(context, request))

def setTipoPropuesta(request, id, tipo):
	propuesta = Propuesta.objects.get(id = id)
	propuesta.estado = tipo
	propuesta.save()
	propuestas = Propuesta.objects.filter(estado = tipo)
	context = {'propuestas': propuestas}
	template = loader.get_template('projectes/propuestas_menu.html')
	return HttpResponse(template.render(context, request))

def propuestas_menu(request):
	propuestas = Propuesta.objects.filter(~Q(estado = 4))
	context = {'propuestas': propuestas}
	template = loader.get_template('projectes/propuestas_menu.html')
	return HttpResponse(template.render(context, request))

def proyectos_menu(request):
	proyectos = Propuesta.objects.all()
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
	objeto1 = Objetivo.objects.all()

	if tipo == '0':
		proyectos = Propuesta.objects.all()
	if tipo == '1':
		proyectos = Propuesta.objects.filter(objetivo = objeto1[0])
	if tipo == '2':
		proyectos = Propuesta.objects.filter(objetivo = objeto1[1])
	if tipo == '3':
		proyectos = Propuesta.objects.filter(objetivo = objeto1[2])
	template = loader.get_template('projectes/proyecto_vista.html')
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
	propuesta.estado = 4
	propuesta.save()
	return proyectos_menu(request)

def formPropuesta(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = addPropuestaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			propuesta = Propuesta(
				titol=form.cleaned_data['titol'],
				descripcion=form.cleaned_data['descripcio'],
				data=form.cleaned_data['data'],
				presupuesto=int(form.cleaned_data['presupuesto']),
				responsable=form.cleaned_data['responsable'],
				objetivo=form.cleaned_data['objetivo'],
				principio=form.cleaned_data['principio'],
				evaluacion=form.cleaned_data['evaluacion'])
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