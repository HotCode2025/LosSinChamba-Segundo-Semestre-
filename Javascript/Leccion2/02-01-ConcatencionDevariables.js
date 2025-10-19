var nombre = 'Jose';
var apellido = 'Montes';
var nombreCompleto = nombre + ' ' + apellido;
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel' + ' ' + 'Betancud'; // Segunda Concatenación
console.log(nombreCompleto2);

var juntos = nombre + 219; // Lee de izq a der siguiendo la cadena lee el numero como str
console.log(juntos);

juntos = nombre + (78 + 17); // Aquí se puede diferenciar a través parentecis
console.log(juntos);

juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;
console.log(nombre);

nombre += apellido; //Tercera Concatenación usando el operador simplificado
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes";
//apellido2 = "Peres"; // una constante no puede ser modificada
console.log(apellido2);

let x, y; // Se pueden crear varias variables dentro de una misma línea
x = 17, y = 21; // Se puede hacer asignación de varias variables dentro de la misma línea
let z = x + y; // Se asigna el valor de la operación
console.log(z);

let _1num = 31;
let rompiendo = "rompe";  //No utilizar palabras reservadas para variables

console.log(_1num)
console.log(rompiendo)





