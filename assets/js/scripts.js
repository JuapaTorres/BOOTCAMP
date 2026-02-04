$(document).ready(function () {
  // 1. LOGIN
  $("#loginForm").submit(function (e) {
    e.preventDefault();
    const email = $("#email").val();
    const pass = $("#password").val();
    if (email === "admin@email.com" && pass === "12345") {
      window.location.href = "html/menu.html";
    } else {
      $("#alert-container").html(
        '<div class="alert alert-danger">Error de acceso</div>',
      );
    }
  });

  // 2. AUTOCOMPLETADO (Filtro dinámico de jQuery)
  $("#busqueda-contacto").on("keyup", function () {
    let value = $(this).val().toLowerCase();
    $("#lista-contactos li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });

  // 3. SELECCIÓN DE CONTACTO
  $(document).on("click", ".contact-item", function () {
    $("#nombre-destino").text($(this).data("nombre"));
    $("#seccion-envio").hide().removeClass("d-none").fadeIn();
  });

  // 4. LÓGICA DE SALDO
  function cargarSaldo() {
    let saldo = parseFloat(localStorage.getItem("miSaldo")) || 50000; // Saldo inicial de prueba
    $("#saldo-menu, #saldo-actual").text("$" + saldo.toLocaleString("es-CL"));
  }

  $("#btn-confirmar-envio").click(function () {
    let monto = parseFloat($("#monto-enviar").val());
    let saldo = parseFloat(localStorage.getItem("miSaldo")) || 50000;

    if (monto > 0 && monto <= saldo) {
      localStorage.setItem("miSaldo", saldo - monto);
      alert("Envío exitoso");
      window.location.href = "menu.html";
    } else {
      alert("Monto inválido o saldo insuficiente");
    }
  });

  cargarSaldo(); // Ejecutar al cargar

  // REDIRECCIONES CON EFECTO
  $("#btn-depositar").click(() => (window.location.href = "deposit.html"));
  $("#btn-enviar").click(() => (window.location.href = "sendmoney.html"));
  $("#btn-movimientos").click(
    () => (window.location.href = "transactions.html"),
  );
});
//Control de flujo de login
