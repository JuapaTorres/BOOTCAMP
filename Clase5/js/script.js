//console.log("Hola desde JavaScript!")

//let expresion = 5 * 3 
//console.log(expresion)
/*
let numero1 = "5"
let numero2 = 5
console.log(numero1 === numero2)*/

/*
let numero1 = 1
let numero2 = 5
let numero3 = 10
console.log(numero1<numero2 && numero2<numero3)*/





/*function sumar(){
    let sumar = 2 + 5
    console.log(sumar)
}

sumar()*/

const btn = document.getElementById('btnIngresar')

const login = () => {
const usuario = document.getElementById('usuario').value
const password = document.getElementById('password').value
const mensaje = document.getElementById('mensaje')

mensaje.innerHTML = usuario === "admin" && password === "1234"
? '<div class="alert alert-success" role="alert">✅¡Acceso permitido!</div>'
: '<div class="alert alert-danger" role="alert">❌¡Acceso denegado!</div>';
}

btn.addEventListener('click', login)