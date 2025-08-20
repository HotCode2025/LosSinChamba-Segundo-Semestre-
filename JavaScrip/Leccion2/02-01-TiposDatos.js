// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamos que es identica
*/
var nombre = 'Leandro';  //Tipo Str
console.log(nombre);

var numero = 5000;    // Tipo Numerico
console.log(numero);

var objeto = {
    nombre : "Teo",
    Raza   : "CallejeroAleman",
    Cedula : "1212",

}

console.log(objeto)

//Tipos de Datos Boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion); 

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo); 

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Chevrolet', 'Audi', 'BMW', 'Ford'];
console.log(autos);
console.log(typeof autos) //Preg. que tipo de dato es:

var z = '';
console.log(z); //Esto se refierea que es una cadena vacia:
console.log(typeof z);
