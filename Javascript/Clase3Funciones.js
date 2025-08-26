// Clase 3 parte 1 Javascript

// miFuncion(8, 2)

function miFuncion(a, b) {
  //console.log("Sumamos: " + (a + b))
  return a + b
}

// llamando la funcion
miFuncion(5, 4)

// Clase 3 parte 2
let resultado = miFuncion(6, 7)
console.log(resultado)

// Clase 3 parte 3
let x = function(a, b) { return a+b };
let resultado2 = x(5, 6)
console.log(resultado2)

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



