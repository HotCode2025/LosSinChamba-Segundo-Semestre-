// Clase 3 parte 1 Javascript

// miFuncion(8, 2)

function miFuncion(a, b) {
  //console.log("Sumamos: " + (a + b))
  return a + b
}

// llamando la funcion
miFuncion(5, 4)

//Clase 3 parte 
let resultado = miFuncion(6, 7);
console.log(resultado); // 13

//Declaramos una función de tipo expresión
let x = function(a, b){ return a + b};
resultado = x(5, 6);
console.log(resultado); 

// Clase 3 parte 4
// Funciones de tipo self e invoking
(function(a, b){
  console.log("Ejecutando la funcion: " + (a + b))
})(9, 6)

console.log(typeof miFuncion)

// Clase 3 parte 5
function miFuncion2(a, b) {
  console.log(arguments.length)
}

miFuncion2(5, 7, 3, 6)

// toString
var miFuncionTexto = miFuncion2.toString()
console.log(miFuncionTexto)

// Clase 3 parte 6
//funciones flecha 
const sumarFuncionFlecha= (a,b)=>a + b;
resultado= sumarFuncionFlecha(3,7);
console.log(resultado);
//clase 3 parte 7 
let sumar = function(a = 4,b =8 ){
    console.log(arguments[0]);
    console.log(arguments[1]);
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);
//clase 3 parte 8

let respuesta  =sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for( let i = 0; i < arguments.length; i++){
        suma += arguments[i];
    }
    return suma;
}
//clase 3 parte 9
let k = 10;
function cambiarValor(a){
    a = 20;
}
cambiarValor(k);
console.log(k);
//clase 3 parte 10
const persona = {
    nombre: "Juan",
    apellido: "lopez"
}
console.log(persona)
function cambiarValorObjeto(p1){
    p1.nombre = "Ignacio";
    p1.apellido = "Perez";
}
cambiarValorObjeto(persona);
console.log(persona)
