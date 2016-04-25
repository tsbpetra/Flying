from django import forms
import datetime
from django.forms.extras.widgets import SelectDateWidget
from .eleccions import * 
from .models import Principio

class addPropuestaForm(forms.Form):
	titol = forms.CharField(label="Titulo propuesta",max_length=200, required=True)
	descripcio = forms.CharField(label="Descripcion",max_length=500, required=True, widget= forms.TextInput(attrs={'style': 'width:100%'}))
	data = forms.DateField(widget=SelectDateWidget, label="Fecha propuesta")
	presupuesto = forms.IntegerField(label="Presupuesto", required=True)
	responsable = forms.CharField(label="Responsable",max_length=200, required=True)
	principio = forms.ModelChoiceField(queryset=Principio.objects.all(), required=True)