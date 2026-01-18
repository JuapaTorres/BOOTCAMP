$(document).ready(function() {
    // --- LÓGICA DE LOGIN ---
    $('#loginForm').submit(function(event) {
        event.preventDefault(); // Evita que la página se recargue

        // Uso de Selectores de jQuery para obtener valores
        var email = $('#email').val();
        var password = $('#password').val();

        // Limpiar alertas previas
        $('#alert-container').empty();

        // Verificación de credenciales (simulada)
        if (email === 'usuario@email.com' && password === '12345') {
            
            // Uso de alerta de Bootstrap (Éxito)
            $('#alert-container').html(`
                <div class="alert alert-success" role="alert">
                    ¡Ingreso exitoso! Redirigiendo al menú...
                </div>
            `);

            // Redirección con jQuery/JS después de 1.5 segundos
            setTimeout(function() {
                window.location.href = 'HTML/menu.html';
            }, 1500);

        } else {
            // Uso de alerta de Bootstrap (Error)
            $('#alert-container').html(`
                <div class="alert alert-danger" role="alert">
                    Usuario o contraseña incorrectas.
                </div>
            `);
        }
    });
});