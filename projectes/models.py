# -*- coding: utf-8 -*-

from django.db import models
from .eleccions import * 

class Principio(models.Model):
	titol=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=200)
	def __str__(self):
		return unicode(self.titol).encode('utf-8')
	
class Objetivo(models.Model):
	nom=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=500)
	principio=models.ForeignKey(Principio, on_delete=models.CASCADE)
	def __str__(self):
		return unicode(self.nom).encode('utf-8')

class Evaluacion(models.Model):
	titol=models.CharField(max_length=200)
	nota_real=models.IntegerField(default=0)
	nota_esperada=models.IntegerField(default=0)
	comentari=models.CharField(max_length=500)
	dresponsabilidad = models.CharField(max_length=200)
	nresponsabilidad=models.IntegerField(default=0)
	destrategia = models.CharField(max_length=200)
	nestrategia=models.IntegerField(default=0)
	dadquisicion = models.CharField(max_length=200)
	nadquisicio=models.IntegerField(default=0)
	drendimiento = models.CharField(max_length=200)
	nrendimiento=models.IntegerField(default=0)
	dconformidad = models.CharField(max_length=200)
	nconformidad=models.IntegerField(default=0)
	dconducta = models.CharField(max_length=200)
	nconducta=models.IntegerField(default=0)
	def __str__(self):
		return unicode(self.titol).encode('utf-8')

class Propuesta(models.Model):
	titol=models.CharField(max_length=200)
	descripcion=models.CharField(max_length=500)
	data=models.DateTimeField('date published')
	presupuesto=models.IntegerField(default=0)
	responsable=models.CharField(max_length=200)
	objetivo=models.ForeignKey(Objetivo, on_delete=models.CASCADE)
	principio=models.ForeignKey(Principio, on_delete=models.CASCADE)
	evaluacion =models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
	estado = models.IntegerField(default=1, choices=STATUS_CHOICES_P)
	def __str__(self):
		return unicode(self.titol).encode('utf-8')

class Metrica(models.Model):
	dades=models.CharField(max_length=2000)
	descripcio=models.CharField(max_length=500)
	proyecto=models.ForeignKey(Propuesta, on_delete=models.CASCADE)
	tipo = models.IntegerField(default=1, choices=STATUS_CHOICES_M)
	def __str__(self):
		return unicode(self.descripcio).encode('utf-8')

class Alerta(models.Model):
	titol=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=200)
	data=models.DateTimeField('date published')
	llegit=models.IntegerField(default=0)
	projecte=models.ForeignKey(Propuesta, on_delete=models.CASCADE)
	metrica=models.ForeignKey(Metrica, on_delete=models.CASCADE)
	prioridad = models.IntegerField(default=1, choices=STATUS_CHOICES_A)
