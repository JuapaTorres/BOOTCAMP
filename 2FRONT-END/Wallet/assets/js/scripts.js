$(document).ready(function() {
    console.log("Sistema Wallet Cargado - Formato de moneda activado");

    // LOGIN (index.html)
    $('#loginForm').submit(function(event) {
        event.preventDefault();
        var correo = $('#email').val();
        var clave = $('#password').val();
        $('#alert-container').empty();

        if (correo === 'admin@email.com' && clave === '12345') {
            $('#alert-container').html('<div class="alert alert-success">¡Éxito! Entrando al sistema...</div>');
            setTimeout(function() {
                window.location.href = 'HTML/menu.html';
            }, 1500);
        } else {
            $('#alert-container').html('<div class="alert alert-danger">Datos incorrectos.</div>');
        }
    });

    // MENÚ PRINCIPAL (menu.html)
    if (window.location.pathname.includes('menu.html')) {
        let saldoGuardado = parseFloat(localStorage.getItem('miSaldo')) || 0;
        $('#saldo-menu').text('$' + saldoGuardado.toLocaleString('es-CL'))
    }
    $(document).on('click', '#btn-depositar', function() {
        $('#redireccion-mensaje').text('Cargando pantalla de Depósito...').removeClass('d-none');
        setTimeout(function() { window.location.href = 'deposit.html'; }, 1000);
    });

    $(document).on('click', '#btn-enviar', function() {
        $('#redireccion-mensaje').text('Cargando Agenda de Contactos...').removeClass('d-none');
        setTimeout(function() { window.location.href = 'sendmoney.html'; }, 1000);
    });

    $(document).on('click', '#btn-movimientos', function() {
        $('#redireccion-mensaje').text('Cargando Historial...').removeClass('d-none');
        setTimeout(function() { window.location.href = 'transactions.html'; }, 1000);
    });

    // DEPÓSITO (deposit.html)
    if (window.location.pathname.includes('deposit.html')) {
        let saldoActual = parseFloat(localStorage.getItem('miSaldo')) || 0;
        $('#saldo-actual').text(saldoActual.toLocaleString('es-CL'));
    }

    $('#depositForm').submit(function(e) {
        e.preventDefault();
        let montoIngresado = parseFloat($('#monto').val());
        let saldoViejo = parseFloat(localStorage.getItem('miSaldo')) || 0;

        if (montoIngresado > 0) {
            let saldoNuevo = saldoViejo + montoIngresado;
            localStorage.setItem('miSaldo', saldoNuevo);

            $('#confirmacion-deposito').text('Has depositado: $' + montoIngresado.toLocaleString('es-CL'));
            $('#alert-container').html('<div class="alert alert-success">¡Saldo actualizado exitosamente!</div>');

            setTimeout(function() { window.location.href = 'menu.html'; }, 2000);
        }
    });

    // ENVIAR DINERO (sendmoney.html)
    function esRutValido(rut) {
        const regex = /^[0-9]{7,8}-[0-9Kk]{1}$/;
        return regex.test(rut);
    }

    $('#btn-mostrar-nuevo').click(function() {
        $('#form-nuevo-contacto').removeClass('d-none').slideDown();
    });

    $('#btn-guardar-contacto').click(function() {
        let nombre = $('#nuevo-nombre').val();
        let rut = $('#nuevo-rut').val();
        if (nombre !== "" && esRutValido(rut)) {
            $('#lista-contactos').prepend('<li class="list-group-item list-group-item-action contact-item" data-nombre="'+nombre+'">' + nombre + ' (RUT: ' + rut + ')</li>');
            $('#nuevo-nombre, #nuevo-rut').val('');
            $('#form-nuevo-contacto').slideUp();
        } else {
            alert("RUT inválido. Use formato 12345678-9");
        }
    });

    $(document).on('click', '.contact-item', function() {
        let nombreSeleccionado = $(this).data('nombre');
        let saldoDisponible = parseFloat(localStorage.getItem('miSaldo')) || 0;

        $('#nombre-destino').text(nombreSeleccionado);
        $('#seccion-envio').removeClass('d-none').fadeIn();
        console.log("Saldo disponible para enviar: $" + saldoDisponible.toLocaleString('es-CL'));
    });

    $('#btn-confirmar-envio').click(function() {
        let montoAEnviar = parseFloat($('#monto-enviar').val());
        let saldoEnCuenta = parseFloat(localStorage.getItem('miSaldo')) || 0;

        if (montoAEnviar <= saldoEnCuenta && montoAEnviar > 0) {
            let saldoRestante = saldoEnCuenta - montoAEnviar;
            localStorage.setItem('miSaldo', saldoRestante);
            
            alert("Has enviado $" + montoAEnviar.toLocaleString('es-CL') + " correctamente.");
            
            $('#msg-exito-envio').removeClass('d-none');
            setTimeout(function() { window.location.href = 'menu.html'; }, 2000);
        } else {
            alert("Saldo insuficiente. Tu saldo es: $" + saldoEnCuenta.toLocaleString('es-CL'));
        }
    });

    // TRANSACCIONES (transactions.html)
    if (window.location.pathname.includes('transactions.html')) {
        const movimientos = [
            { fecha: '2024-05-10', desc: 'Carga de saldo', monto: 50000, tipo: 'deposito' },
            { fecha: '2024-05-12', desc: 'Transferencia a Juan', monto: -15000, tipo: 'transferencia' },
            { fecha: '2024-05-15', desc: 'Pago Supermercado', monto: -8500, tipo: 'compra' }
        ];

        function dibujarTabla(filtro) {
            $('#lista-movimientos').empty();
            movimientos.forEach(function(m) {
                if (filtro === 'todos' || m.tipo === filtro) {
                    let color = m.monto > 0 ? 'text-success' : 'text-danger';
                    // Aquí aplicamos el formato a cada fila de la tabla
                    $('#lista-movimientos').append('<li class="list-group-item d-flex justify-content-between">' + 
                        '<span>' + m.fecha + ' - ' + m.desc + '</span>' +
                        '<strong class="' + color + '">$' + m.monto.toLocaleString('es-CL') + '</strong>' +
                    '</li>');
                }
            });
        }

        dibujarTabla('todos');
        $('#filtro-tipo').change(function() { dibujarTabla($(this).val()); });
    }
});