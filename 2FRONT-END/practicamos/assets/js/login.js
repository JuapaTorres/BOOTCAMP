// 1. Definimos las credenciales correctas (como si estuvieran en una base de datos)
const usuarioValido = "admin";
const contraseñaValida = "12345";

// 2. Solicitamos los datos al usuario
let usuarioIngresado = prompt("Ingrese su nombre de usuario:");
let contraseñaIngresada = prompt("Ingrese su contraseña:");

// 3. Verificamos mediante la estructura de control 'if'
// Usamos el operador lógico && (AND) para que AMBAS condiciones deban cumplirse
if (usuarioIngresado === usuarioValido && contraseñaIngresada === contraseñaValida) {
    alert("¡Bienvenido, " + usuarioIngresado + "! Inicio de sesión exitoso.");
} else {
    // Si uno de los dos (o ambos) es incorrecto, entra aquí
    alert("Error: Usuario o contraseña incorrectos. Intente de nuevo.");
}

