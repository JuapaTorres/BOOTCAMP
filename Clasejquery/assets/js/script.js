$(document).ready(function() {

    $('#boton-abrir').on('click', function() {
        $('#modal-fondo').show();
    });

    $('#botonX').on('click', function() {
        $('#modal-fondo').hide();
    });

    $('#boton-cerrar').on('click', function() {
        $('#modal-fondo').hide();
    });

});