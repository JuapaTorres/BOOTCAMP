$(document).ready(function () {
  //FUNCIONES DE APOYO

  //Guarda una transacción en el historial
  function guardarTransaccion(tipo, monto, desc) {
    let movimientos = JSON.parse(localStorage.getItem("movimientos")) || [];
    const nuevaTransa = {
      fecha: new Date().toLocaleDateString('es-CL'),
      tipo: tipo, //"deposito", "transferencia", "compra"
      monto: monto,
      desc: desc
    };
    movimientos.unshift(nuevaTransa); //Agrega al principio de la lista
    localStorage.setItem("movimientos", JSON.stringify(movimientos));
  }

  //Carga el saldo en las pantallas donde sea necesario
  function cargarSaldo() {
    let saldo = parseFloat(localStorage.getItem("miSaldo"));
    //Si es la primera vez (null), inicializamos en 50000
    if (isNaN(saldo)) {
      saldo = 50000;
      localStorage.setItem("miSaldo", saldo);
    }
    $("#saldo-menu, #saldo-actual").text("$" + saldo.toLocaleString("es-CL"));
  }

  //LOGIN (index.html)
  $("#loginForm").submit(function (e) {
    e.preventDefault();
    const email = $("#email").val();
    const pass = $("#password").val();
    if (email === "admin@email.com" && pass === "12345") {
      window.location.href = "html/menu.html";
    } else {
      $("#alert-container").html(
        '<div class="alert alert-danger">Error de acceso. Verifique sus datos.</div>'
      );
    }
  });

  //DEPOSITO (deposit.html)
  $("#depositForm").submit(function (e) {
    e.preventDefault();
    let monto = parseFloat($("#monto").val());
    let saldoActual = parseFloat(localStorage.getItem("miSaldo")) || 0;

    if (monto > 0) {
      let nuevoSaldo = saldoActual + monto;
      localStorage.setItem("miSaldo", nuevoSaldo);
      
      //Registrar en historial
      guardarTransaccion('deposito', monto, 'Depósito de efectivo');

      $("#confirmacion-deposito").text("Has depositado: $" + monto.toLocaleString("es-CL"));
      setTimeout(() => { window.location.href = "menu.html"; }, 1500);
    } else {
      alert("Ingrese un monto válido");
    }
  });

  //ENVIAR DINERO (sendmoney.html)
  
  //Autocompletado
  $("#busqueda-contacto").on("keyup", function () {
    let value = $(this).val().toLowerCase();
    $("#lista-contactos li").filter(function () {
      $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
    });
  });

  //Mostrar formulario nuevo contacto
  $("#btn-mostrar-nuevo").click(function() {
    $("#form-nuevo-contacto").removeClass("d-none").hide().slideDown();
  });

  //Guardar nuevo contacto y que quede registraado
  $("#btn-guardar-contacto").click(function() {
    let nombre = $("#nuevo-nombre").val();
    let rut = $("#nuevo-rut").val();
    if (nombre && rut) {
      $("#lista-contactos").prepend(`
        <li class="list-group-item list-group-item-action contact-item" data-nombre="${nombre}">
          ${nombre} (RUT: ${rut})
        </li>
      `);
      $("#nuevo-nombre, #nuevo-rut").val("");
      $("#form-nuevo-contacto").slideUp();
    }
  });

  //Seleccionar contacto
  $(document).on("click", ".contact-item", function () {
    $("#nombre-destino").text($(this).data("nombre"));
    $("#seccion-envio").hide().removeClass("d-none").fadeIn();
  });

  //Confirmar Envío
  $("#btn-confirmar-envio").click(function () {
    let monto = parseFloat($("#monto-enviar").val());
    let saldo = parseFloat(localStorage.getItem("miSaldo")) || 0;
    let destino = $("#nombre-destino").text();

    if (monto > 0 && monto <= saldo) {
      localStorage.setItem("miSaldo", saldo - monto);
      
      //Registrar en historial, para que se muestren todos los movimientos
      guardarTransaccion('transferencia', monto, 'Envío a ' + destino);

      alert("Envío exitoso");
      window.location.href = "menu.html";
    } else {
      alert("Monto inválido o saldo insuficiente");
    }
  });

  //HISTORIAL (transactions.html)
  if (window.location.pathname.includes("transactions.html")) {
    function dibujarTabla(filtro = "todos") {
      let movimientos = JSON.parse(localStorage.getItem("movimientos")) || [];
      $("#lista-movimientos").empty();

      movimientos.forEach(m => {
        if (filtro === "todos" || m.tipo === filtro) {
          let esGasto = (m.tipo === 'transferencia' || m.tipo === 'compra');
          let colorClass = esGasto ? "text-danger" : "text-success";
          let signo = esGasto ? "-" : "+";

          $("#lista-movimientos").append(`
            <li class="list-group-item d-flex justify-content-between align-items-center">
              <div>
                <small class="text-muted d-block">${m.fecha}</small>
                <strong>${m.desc}</strong>
              </div>
              <span class="${colorClass} fw-bold">${signo} $${m.monto.toLocaleString("es-CL")}</span>
            </li>
          `);
        }
      });
    }

    dibujarTabla();
    $("#filtro-tipo").change(function() { dibujarTabla($(this).val()); });
  }

  //INICIALIZACIÓN GENERAL
  cargarSaldo();

  //Botones para redireccionar a otras pantallas
  $("#btn-depositar").click(() => (window.location.href = "deposit.html"));
  $("#btn-enviar").click(() => (window.location.href = "sendmoney.html"));
  $("#btn-movimientos").click(() => (window.location.href = "transactions.html"));
});