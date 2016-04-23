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
function generarProyecto(id){
	$.ajax({
		url: 'propuestas/'+id,
		success: function(data) {
			enlacePropuestas();
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
enlaceAlertes();