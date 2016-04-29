function revisadas(){
	$.ajax({
		url: 'alertas/1',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function todas(){
	$.ajax({
		url: 'alertas/2',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function pendientes(){
	$.ajax({
		url: 'alertas/0',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function marcarrevisado(id){
	$.ajax({
		url: 'setVisto/'+id,
		success: function(data) {
			todas();
		}
	});
}

function enlaceObjetivos(){
	$.ajax({
		url: 'objetivos',
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}

function enlacePrincipios(){
	$.ajax({
		url: 'principios',
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}

function generarProyecto(id){
	$.ajax({
		url: 'propuestas/'+id,
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}
function enlacePropuestas(){
	$.ajax({
		url: 'propuestas',
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}
function enlacePropuestasTipo(id){
	$.ajax({
		url: 'propuestas/get/'+id,
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}
function enlaceProyectos(){
	$.ajax({
		url: 'proyectos',
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}

function o_proyectos(){
	var tipo = 0;
	if (document.getElementById('innovacion').checked) {
		tipo = tipo + 1;
	}
	if (document.getElementById('calidad').checked) {
		tipo = tipo + 2;
	}
	if (document.getElementById('confianza').checked) {
		tipo = tipo + 4;
	}
	$.ajax({
		url: 'proyectos/'+tipo,
		success: function(data) {
			$('#cont_proyectos').html(data);
		}
	});
}
function enlaceAlertes(){
	$.ajax({
		url: 'alertas',
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}
function abrirProyecto(id){
	$.ajax({
		url: 'proyectos/proyecto/'+id,
		success: function(data) {
			$('#page-wrapper').html(data);
		}
	});
}
function getForm(){
	$.ajax({
		url: 'propuestas/add',
		success: function(data) {
			$('#modal_form').html(data);
		}
	});
}

function getFormObjetivo(){
	$.ajax({
		url: 'objetivos/add',
		success: function(data) {
			$('#modal_form').html(data);
		}
	});
}

function getFormPrincipio(){
	$.ajax({
		url: 'principio/add',
		success: function(data) {
			$('#modal_form').html(data);
		}
	});
}

function calidad(){
	$.ajax({
		url: 'proyectos/3',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function todas_p(){
	$.ajax({
		url: 'proyectos/0',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function innov(){
	$.ajax({
		url: 'proyectos/2',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function seguridad(){
	$.ajax({
		url: 'proyectos/1',
		success: function(data) {
			$('#cont_alertas').html(data);
		}
	});
}
function estadoPropuesta(id, estado){
	$.ajax({
		url: 'propuestas/estado/'+id+'/'+estado,
		success: function(data) {
			$('#page-wrapper').html('');
			$('#page-wrapper').html(data);
		}
	});
}

function eliminarObj(id){
	$.ajax({
		url: 'objetivo/eliminar/'+id,
		success: function(data) {
			$('#page-wrapper').html('');
			$('#page-wrapper').html(data);
		}
	});
}

function modificarObj(id){
	$.ajax({
		url: 'objetivo/mod/'+id,
		success: function(data) {
			$('#mod_form').html(data);
		}
	});
}

function modificarPrincipio(id){
	$.ajax({
		url: 'principio/mod/'+id,
		success: function(data) {
			$('#mod_form').html(data);
		}
	});
}

function eliminarPrin(id){
	$.ajax({
		url: 'principio/eliminar/'+id,
		success: function(data) {
			$('#page-wrapper').html('');
			$('#page-wrapper').html(data);
		}
	});
}
enlaceAlertes();