from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget
from .models import Principio, Evaluacion, Objetivo, Propuesta
from .eleccions import STATUS_CHOICES_M


class addPropuestaForm(forms.Form):
	titol = forms.CharField(label="Titulo propuesta",max_length=200, required=True)
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	data = forms.DateField(widget=SelectDateWidget, label="Fecha propuesta")
	presupuesto = forms.IntegerField(label="Presupuesto", required=True)
	responsable = forms.CharField(label="Responsable",max_length=200, required=True)
	principio = forms.ModelChoiceField(queryset=Principio.objects.all(), required=True)
	evaluacion = forms.ModelChoiceField(queryset=Evaluacion.objects.all(), required=True)
	objetivo = forms.ModelChoiceField(queryset=Objetivo.objects.all(), required=True)

class addObjetivoForm(forms.Form):
	nom = forms.CharField(label="Nombre del objetivo",max_length=200, required=True)
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	principio = forms.ModelChoiceField(queryset=Principio.objects.all(), required=True)

class addPrincipioForm(forms.Form):
	titol = forms.CharField(label="Nombre del principio",max_length=200, required=True)
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))

class modObjetivoForm(forms.Form):
	nom = forms.CharField(label="Nombre del objetivo",max_length=200, required=True)
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	principio = forms.ModelChoiceField(queryset=Principio.objects.all(), required=True)

class modPrincipioForm(forms.Form):
	nom = forms.CharField(label="Nombre del principio",max_length=200, required=True)
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))

class addEvaluacionForm(forms.Form):
	titol = forms.CharField(label="Nombre de la evaluacion",max_length=200, required=True)
	nota_real = forms.IntegerField(label="Nota real", required=True)
	nota_esperada = forms.IntegerField(label="Nota esperada", required=True)
	comentari = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	dresponsabilidad = forms.CharField(label="Descripcion responsabilidad",max_length=200, required=True)
	nresponsabilidad = forms.IntegerField(label="Nota responsabilidad", required=True)
	destrategia = forms.CharField(label="Descripcion estrategia",max_length=200, required=True)
	nestrategia = forms.IntegerField(label="Nota estrategia", required=True)
	dadquisicion = forms.CharField(label="Descripcion adquisicion",max_length=200, required=True)
	nadquisicio = forms.IntegerField(label="Nota adquisicion", required=True)
	drendimiento = forms.CharField(label="Descripcion rendimiento",max_length=200, required=True)
	nrendimiento = forms.IntegerField(label="Nota rendimiento", required=True)
	dconformidad = forms.CharField(label="Descripcion conformidad",max_length=200, required=True)
	nconformidad = forms.IntegerField(label="Nota conformidad", required=True)
	dconducta = forms.CharField(label="Descripcion conducta",max_length=200, required=True)
	nconducta = forms.IntegerField(label="Nota conducta", required=True)

class modEvaluacionForm(forms.Form):
	titol = forms.CharField(label="Nombre de la evaluacion",max_length=200, required=True)
	nota_real = forms.IntegerField(label="Nota real", required=True)
	nota_esperada = forms.IntegerField(label="Nota esperada", required=True)
	comentari = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	dresponsabilidad = forms.CharField(label="Descripcion responsabilidad",max_length=200, required=True)
	nresponsabilidad = forms.IntegerField(label="Nota responsabilidad", required=True)
	destrategia = forms.CharField(label="Descripcion estrategia",max_length=200, required=True)
	nestrategia = forms.IntegerField(label="Nota estrategia", required=True)
	dadquisicion = forms.CharField(label="Descripcion adquisicion",max_length=200, required=True)
	nadquisicio = forms.IntegerField(label="Nota adquisicion", required=True)
	drendimiento = forms.CharField(label="Descripcion rendimiento",max_length=200, required=True)
	nrendimiento = forms.IntegerField(label="Nota rendimiento", required=True)
	dconformidad = forms.CharField(label="Descripcion conformidad",max_length=200, required=True)
	nconformidad = forms.IntegerField(label="Nota conformidad", required=True)
	dconducta = forms.CharField(label="Descripcion conducta",max_length=200, required=True)
	nconducta = forms.IntegerField(label="Nota conducta", required=True)

class addMetricaForm(forms.Form):
	descripcio = forms.CharField(label="Descripcion", max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	proyecto = forms.ModelChoiceField(queryset=Propuesta.objects.all(), required=True)
	tipo = forms.ChoiceField(choices=(STATUS_CHOICES_M), required=False)

class modMetricaForm(forms.Form):
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	proyecto = forms.ModelChoiceField(queryset=Propuesta.objects.all(), required=True)
	tipo = forms.ChoiceField(choices=(STATUS_CHOICES_M), required=False)
