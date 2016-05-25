from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.utils import timezone
from .forms import addPropuestaForm, addObjetivoForm, modObjetivoForm, modPrincipioForm, addPrincipioForm, addEvaluacionForm, modEvaluacionForm, addMetricaForm, modMetricaForm
from django.db.models import Q
import json
from django.http import JsonResponse


def index(request):
    template = loader.get_template('projectes/index.html')
    return HttpResponse(template.render(request))

def alertas_menu(request):
	alertas = Alerta.objects.filter(llegit=0)
	context = {'alertas': alertas}
	template = loader.get_template('projectes/alertas_menu.html')
	return HttpResponse(template.render(context, request))

def generarOjetivos(request):
	objetivo = Objetivo.objects.all()
	context = {'objetivo': objetivo}
	template = loader.get_template('projectes/objetivos_menu.html')
	return HttpResponse(template.render(context, request))

def generarPrincipios(request):
	objetivo = Principio.objects.all()
	context = {'objetivo': objetivo}
	template = loader.get_template('projectes/principios_menu.html')
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

def eliminarObj(request, id):
	obj = Objetivo.objects.get(id = id)
	obj.delete()
	objetivo = Objetivo.objects.all()
	context = {'objetivo': objetivo}
	template = loader.get_template('projectes/objetivos_menu.html')
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

def formObjetivo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = addObjetivoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			obj = Objetivo(
				nom=form.cleaned_data['nom'],
				descripcio=form.cleaned_data['descripcio'],
				principio=form.cleaned_data['principio'])
			obj.save()
			return HttpResponseRedirect('..')
    else:
		form = addObjetivoForm()

    return render(request, 'projectes/form_obj.html', {'form': form})

def formPrincipio(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = addPrincipioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			obj = Principio(
				titol=form.cleaned_data['titol'],
				descripcio=form.cleaned_data['descripcio'])
			obj.save()
			return HttpResponseRedirect('..')
    else:
		form = addPrincipioForm()

    return render(request, 'projectes/form_prin.html', {'form': form})

def selectProyecto(request, id):
	proyecto = Propuesta.objects.get(id=id)
	context = {'proyecto': proyecto}
	template = loader.get_template('projectes/selectProyecto.html')
	return HttpResponse(template.render(context, request))


def modificarObj(request, id):
    # if this is a POST request we need to process the form data
    item = Objetivo.objects.get(id=id)
    if request.method == 'POST':
        form = modObjetivoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			item.nom=form.cleaned_data['nom']
			item.descripcio=form.cleaned_data['descripcio']
			item.principio=form.cleaned_data['principio']
			item.save()
			return HttpResponseRedirect('../../..')
    else:
		form = modObjetivoForm(initial={'nom': item.nom, 'descripcio': item.descripcio, 'principio': item.principio})


    return render(request, 'projectes/form_obj_mod.html', {'form': form, 'item':id})

def modificarPrincipio(request, id):
    # if this is a POST request we need to process the form data
    item = Principio.objects.get(id=id)
    if request.method == 'POST':
        form = modPrincipioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			item.titol=form.cleaned_data['nom']
			item.descripcio=form.cleaned_data['descripcio']
			item.save()
			return HttpResponseRedirect('../../..')
    else:
		form = modPrincipioForm(initial={'nom': item.titol, 'descripcio': item.descripcio})


    return render(request, 'projectes/form_prin_mod.html', {'form': form, 'item':id})

def eliminarPrin(request, id):
	obj = Principio.objects.get(id = id)
	obj.delete()
	objetivo = Principio.objects.all()
	context = {'objetivo': objetivo}
	template = loader.get_template('projectes/principios_menu.html')
	return HttpResponse(template.render(context, request))

def presupuestos_menu(request):
	proyectos = Propuesta.objects.all()
	context = {'proyectos': proyectos}
	template = loader.get_template('projectes/presupuestos_menu.html')
	return HttpResponse(template.render(context, request))

def metricas_menu(request):
	metricas = Metrica.objects.all()
	context = {'metricas': metricas}
	template = loader.get_template('projectes/metricas_menu.html')
	return HttpResponse(template.render(context, request))

def evaluaciones_menu(request):
	evaluaciones = Evaluacion.objects.all()
	context = {'evaluaciones': evaluaciones}
	template = loader.get_template('projectes/evaluaciones_menu.html')
	return HttpResponse(template.render(context, request))

def selectEvaluacion(request, id):
	evaluacion = Evaluacion.objects.get(id=id)
	context = {'evaluacion': evaluacion}
	template = loader.get_template('projectes/selectEvaluacion.html')
	return HttpResponse(template.render(context, request))

def formEvaluacion(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = addEvaluacionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			evaluacion = Evaluacion(
                titol=form.cleaned_data['titol'],
            	nota_real=int(form.cleaned_data['nota_real']),
            	nota_esperada=int(form.cleaned_data['nota_esperada']),
            	comentari=form.cleaned_data['comentari'],
            	dresponsabilidad=form.cleaned_data['dresponsabilidad'],
            	nresponsabilidad=int(form.cleaned_data['nresponsabilidad']),
            	destrategia=form.cleaned_data['destrategia'],
            	nestrategia=int(form.cleaned_data['nestrategia']),
            	dadquisicion=form.cleaned_data['dadquisicion'],
            	nadquisicio=int(form.cleaned_data['nadquisicio']),
            	drendimiento=form.cleaned_data['drendimiento'],
            	nrendimiento=int(form.cleaned_data['nrendimiento']),
            	dconformidad=form.cleaned_data['dconformidad'],
            	nconformidad=int(form.cleaned_data['nconformidad']),
            	dconducta=form.cleaned_data['dconducta'],
            	nconducta=int(form.cleaned_data['nconducta']))
			evaluacion.save()
			return HttpResponseRedirect('..')
    else:
		form = addEvaluacionForm()

    return render(request, 'projectes/form_evaluacion.html', {'form': form})


def modificarEvaluacion(request, id):
    item = Evaluacion.objects.get(id = id)
    if request.method == 'POST':
        form = modEvaluacionForm(request.POST)
        if form.is_valid():
            item.titol=form.cleaned_data['titol']
            item.nota_real=form.cleaned_data['nota_real']
            item.nota_esperada=form.cleaned_data['nota_esperada']
            item.comentari=form.cleaned_data['comentari']
            item.dresponsabilidad=form.cleaned_data['dresponsabilidad']
            item.nresponsabilidad=form.cleaned_data['nresponsabilidad']
            item.destrategia=form.cleaned_data['destrategia']
            item.nestrategia=form.cleaned_data['nestrategia']
            item.dadquisicion=form.cleaned_data['dadquisicion']
            item.nadquisicio=form.cleaned_data['nadquisicio']
            item.drendimiento=form.cleaned_data['drendimiento']
            item.nrendimiento=form.cleaned_data['nrendimiento']
            item.dconformidad=form.cleaned_data['dconformidad']
            item.nconformidad=form.cleaned_data['nconformidad']
            item.dconducta=form.cleaned_data['dconducta']
            item.nconducta=form.cleaned_data['nconducta']
            item.save()
            return HttpResponseRedirect('../../..')
    else:
            form = modEvaluacionForm(initial={'titol': item.titol, 'nota_real': item.nota_real, 'nota_esperada': item.nota_esperada, 'comentari': item.comentari, 'dresponsabilidad': item.dresponsabilidad, 'nresponsabilidad': item.nresponsabilidad, 'destrategia': item.destrategia, 'nestrategia': item.nestrategia, 'dadquisicion': item.dadquisicion, 'nadquisicio': item.nadquisicio, 'drendimiento': item.drendimiento, 'nrendimiento': item.nrendimiento, 'dconformidad': item.dconformidad, 'nconformidad': item.nconformidad, 'dconducta': item.dconducta, 'nconducta': item.nconducta})

    return render(request, 'projectes/form_evaluacion_mod.html', {'form': form, 'item': id})


def eliminarEvaluacion(request, id):
	evaluacion = Evaluacion.objects.get(id = id)
	evaluacion.delete()
	evaluaciones = Evaluacion.objects.all()
	context = {'evaluaciones': evaluaciones}
	template = loader.get_template('projectes/evaluaciones_menu.html')
	return HttpResponse(template.render(context, request))

def formMetrica(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = addMetricaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
			metrica = Metrica(
                dades=form.cleaned_data['dades'],
            	descripcio=form.cleaned_data['descripcio'],
            	proyecto=form.cleaned_data['proyecto'],
            	tipo=form.cleaned_data['tipo'])
			metrica.save()
			return HttpResponseRedirect('..')
    else:
		form = addMetricaForm()

    return render(request, 'projectes/form_metrica.html', {'form': form})


def modificarMetrica(request, id):
    item = Metrica.objects.get(id = id)
    if request.method == 'POST':
        form = modMetricaForm(request.POST)
        if form.is_valid():
            item.dades=form.cleaned_data['dades']
            item.descripcio=form.cleaned_data['descripcio']
            item.proyecto=form.cleaned_data['proyecto']
            item.tipo=form.cleaned_data['tipo']
            item.save()
            return HttpResponseRedirect('../../..')
    else:
            form = modMetricaForm(initial={'dades': item.dades, 'descripcio': item.descripcio, 'proyecto': item.proyecto, 'tipo': item.tipo})

    return render(request, 'projectes/form_metrica_mod.html', {'form': form, 'item': id})

def eliminarMetrica(request, id):
	metrica = Metrica.objects.get(id = id)
	metrica.delete()
	metricas = Metrica.objects.all()
	context = {'metricas': metricas}
	template = loader.get_template('projectes/metricas_menu.html')
	return HttpResponse(template.render(context, request))

def selectMetrica(request, id):
	metrica = Metrica.objects.get(id=id)
	context = {'metrica': metrica}
	template = loader.get_template('projectes/selectMetrica.html')
	return HttpResponse(template.render(context, request))

def selectMetricasProjecte(request, id):
	metricas = Metrica.objects.filter(proyecto=id)
	response = ""
	for m in metricas:
		response = response + m.dades +"#"
 	return HttpResponse(response)

def selectPresupostsProjectes(request):
    proyectos = Propuesta.objects.all()
    response = "["
    for p in proyectos:
        response = response + "{name: '" + p.titol + "' , y: " + str(p.presupuesto) + "}, "
    response = response + "]"
    return HttpResponse(response)

def selectObjetivoProyecto(request, id):
	propuestas = Propuesta.objects.filter(Q(objetivo=id) & Q(estado=4))
	evaluacion = "["
	response = "["
	categories = "["
	evaluacion_esperada = "["
	for x in propuestas:
		categories = categories + "'"+x.titol+"',"
		evaluacion = evaluacion + "{name: Nota real , data: " + str(x.evaluacion.nota_real) + "}, "
		evaluacion_esperada = evaluacion_esperada + "{name: Nota esperada , data: " + str(x.evaluacion.nota_esperada) + "}, "
		response = response + "{name: '" + x.titol + "' , y: " + str(x.presupuesto) + "}, "
	response = response + "]"
	categories = categories + "]"
	evaluacion = evaluacion + "]"
	evaluacion_esperada = evaluacion_esperada + "]"
	
	context = {'response': response, 'evaluacion': evaluacion, 'categories': categories,'id': id}
	template = loader.get_template('projectes/comparacion.html')
	return HttpResponse(template.render(context, request))
