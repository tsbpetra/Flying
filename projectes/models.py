# -*- coding: utf-8 -*-

from django.db import models

class Principio(models.Model):
	titol=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=200)
	def __str__(self):
		return unicode(self.titol).encode('utf-8')
	
class Objetivo(models.Model):
	nom=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=500)
	principio=models.ForeignKey(Principio, on_delete=models.CASCADE)

class Propuesta(models.Model):
	titol=models.CharField(max_length=200)
	descripcion=models.CharField(max_length=500)
	data=models.DateTimeField('date published')
	presupuesto=models.IntegerField(default=0)
	responsable=models.CharField(max_length=200)
	objetivo=models.ForeignKey(Objetivo, on_delete=models.CASCADE)
	principio=models.ForeignKey(Principio, on_delete=models.CASCADE)
	STATUS_CHOICES = (
		(1, 'Pendiente'),
		(2, 'Rechazada'),
		(3, 'Aplazada'),
	)
	estado = models.IntegerField(default=1, choices=STATUS_CHOICES)

class Proyecto(models.Model):
	titol=models.CharField(max_length=200)
	descripcion=models.CharField(max_length=500)
	data_inicio=models.DateTimeField('Fecha inicio')
	data_fin=models.DateTimeField('Fecha fin')
	presupuesto=models.IntegerField(default=0)

class Evaluacion(models.Model):
	titol=models.CharField(max_length=200)
	nota_real=models.IntegerField(default=0)
	nota_esperada=models.IntegerField(default=0)
	comentari=models.CharField(max_length=500)
	proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)

class Alerta(models.Model):
	titol=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=200)
	data=models.DateTimeField('date published')
	llegit=models.IntegerField(default=0)
	projecte=models.ForeignKey(Proyecto, on_delete=models.CASCADE)
	STATUS_CHOICES = (
		(1, 'Baja'),
		(2, 'Media'),
		(3, 'Alta'),
	)
	prioridad = models.IntegerField(default=1, choices=STATUS_CHOICES)

class Metrica(models.Model):
	ficher=models.CharField(max_length=200)
	descripcio=models.CharField(max_length=500)
	proyecto=models.ForeignKey(Proyecto, on_delete=models.CASCADE)