//Ejercicio 1: Calcular estación del año
let mes = 4;
let estacion; //Undefined
if(mes == 1 || mes == 2 || mes == 12){
    estacion = "Verano";
}
else if(mes == 3 || mes == 4 || mes == 5){
    estacion = "Otoño";
}
else if(mes == 6 || mes == 7 || mes == 8){
    estacion = "Invierno";
}
else if(mes == 9 || mes == 10 || mes == 11){
    estacion = "Primavera";
}
else{
    estacion = "Valor incorrecto";
}
console.log("El valor corresponde a la estación de: " + estacion);

//Ejercicio 2: Hora del día
/*
de 6 a 11 nos saluda: Buenos dias a con todo!
de 12 a 16 nos saluda: A Dormir la siesta
de 17 a 19 nos saluda: Buenas Tardes
de 20 a 23 nos saluda: Hasta Mañana
Trabajaremos con 24 horas
*/
let horaDia = 20;
let mensaje;

if (horaDia >= 6 && horaDia <= 11) {
    mensaje = "Buenos dias a con todo!";
} else if (horaDia >= 12 && horaDia <= 16) {
    mensaje = "A Dormir la siesta";
} else if (horaDia >= 17 && horaDia <= 19) {
    mensaje = "Buenas Tardes";
} else if (horaDia >= 20 && horaDia <= 23) {
    mensaje = "Hasta Mañana";
} else {
    mensaje = "Valor incorrecto";
}
console.log(mensaje);

//Estructura switch (la sintaxis es igual a Java)
switch (mes) {// No solo se pueden utilizar números, también cadenas
    case 1: case 2: case 12:
        estacion = "Verano";
        break;
    case 3: case 4: case 5:
        estacion = "Otoño";
        break;
    case 6: case 7: case 8:
        estacion = "Invierno";
        break;
    case 9: case 10: case 11:
        estacion = "Primavera";
        break;
    default:
        estacion = "Valor incorrecto";
}
console.log("Bienvenido a la estación de: " + estacion);

//Ampliando el uso de var let y const
/*
Con var puedes reasignar en cualquier momento
este forma parte del ambito global
Un error es que se sobreescribe
*/

var nombre = 'Ariel';
nombre = 'Osvaldo';
console.log(nombre);

function saludar() {
    var nombre = 'Natalia';
    console.log(nombre);
}
console.log(nombre); //No lee el dato de la funcion 

if (true) {
    var edad = 34;
    console.log(edad); // 34
}
console.log(edad); //En la función funciono correctamente, estrutura if falla

/*
let: esta puede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una función
*/

function saludar2() {
    let nombre2 = 'Ariel';
    console.log(nombre2);
}

if (true) {
    let edad = 33;
    console.log(edad);
}
/*
const se utiliza para valores constantes que no pueden ser reasignadas
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2003;
//console.log(fechaNacimiento); //solo se ejecuta la ant.

//Evitar repetir tu código
//Dry don't repeat yourself

let days = 'Domingo'
switch (days) {
    case 'Lunes':
        console.log('hoy es ' + days);
        break;
    case 'Martes':
        console.log('hoy es ' + days);
        break;
    case 'Miercoles':
        console.log('hoy es ' + days);
        break;
    case 'Jueves':
        console.log('hoy es ' + days);
        break;
    case 'Viernes':
        console.log('hoy es ' + days);
        break;
    case 'Sábado':
        console.log('hoy es ' + days);
        break;
     case 'Domingo':
        console.log('hoy es ' + days);
        break;
    default:
        break;

}
//Estas es la opcion mejorada
let days2 = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'];
function getDay(n) {
    if (n < 1 || n > 7) {
        throw new Error('out of range');
    }
    return days2[n - 1];
}
console.log(getDay(5));

// 04-01-Ejercicios.js

// Hacer un ejercicio similar al que esta hecho, pero ahora con los
// meses del año, debes hacerlo con la estructura switch y luego con
// la función en la opción mejorada

// Opción con estructura switch para los meses del año
let monthName = 'Marzo'; // Puedes cambiar este valor para probar diferentes meses

switch (monthName) {
    case 'Enero':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Febrero':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Marzo':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Abril':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Mayo':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Junio':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Julio':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Agosto':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Septiembre':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Octubre':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Noviembre':
        console.log('El mes actual es ' + monthName);
        break;
    case 'Diciembre':
        console.log('El mes actual es ' + monthName);
        break;
    default:
        console.log('Mes no reconocido.');
        break;
}

// Esta es la opción mejorada (utilizando una función y un array) para los meses del año
let months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'];

function getMonth(n) {
    if (n < 1 || n > 12) {
        throw new Error('Número de mes fuera de rango (debe ser entre 1 y 12).');
    }
    return months[n - 1];
}

// Ejemplos de uso de la función mejorada:
console.log(getMonth(1)); // Debería imprimir "Enero"
console.log(getMonth(6)); // Debería imprimir "Junio"
console.log(getMonth(12)); // Debería imprimir "Diciembre"

// Prueba con un número fuera de rango para ver el error
try {
    console.log(getMonth(0));
} catch (error) {
    console.error(error.message); // Debería imprimir "Número de mes fuera de rango..."
}

try {
    console.log(getMonth(13));
} catch (error) {
    console.error(error.message); // Debería imprimir "Número de mes fuera de rango..."
}