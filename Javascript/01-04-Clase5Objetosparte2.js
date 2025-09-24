let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
// Objeto
let persona = {
    nombre: 'kevin',
    apellido : 'castilla',
    email: 'kevinrasgido73@gmail.com',
    edad: 29,
    idioma: 'ES',
    get lang(){
        return this.idioma.toUpperCase(); //convierte las minisculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    }, 
    nombreCompleto: function(){ //metodo o funcion en javascript        
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){//este es metodo get
        return 'El nombre es: '+this.nombre+', edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona.nombreCompleto())
console.log('Ejecutando con un objeto');
let persona2 = new Object(); //debe crear un nuevo objeto en memoria
persona2.nombre = 'Valentina'
persona2.direccion = 'bolita 33'
persona2.telefono = '5492942511151'
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']); // accedemos como si fuera un arreglo
console.log('Usamos un ciclo for in');
// for in y accedemos como si fuera un arreglo
for (propiedad in persona){
    console.log(propiedad)
    console.log(persona[propiedad]);
    // acceder a propiedad 
}
console.log('cambiamos y eliminamos un error');
persona.apellido = 'morano';//cambiamos dinamicamente un valor del objeto
//delete persona.apellido; //eliminamo el error
console.log(persona);

//NUmero 1: la mas sencilla: concatenar cada valor de cada propiedad
console.log('Distintas formas de imprimir un objeto forma 1');
console.log(persona.nombre+', '+persona.apellido);

//numero 2: a traves del ciclo for in
console.log('Distintas formas de imprimir un objeto forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);

}

//numero 3: la funcion object.values()
console.log('Distintas formas de imprimir un objeto forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//numero 4: utilizaremos el metodo JSON.stringify
console.log('Distintas formas de imprimir un objeto forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);


//
//CLASE 5 OBJETOS PARTE 2
//


//metodo
console.log('comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);

console.log('Comenzamos con el metodo get y set para idioma');
persona.lang = 'en'; // se cambia en el console
console.log(persona.lang);

function Persona3(nombre = Max, apellido, email){
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Mariano','Lescano','marianorasgido@gmail.com');
padre.nombre = 'Ramiro'; // modificamos el nombre
padre.telefono = '2604010203'; //propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); // utilizamos la funcion
let madre = new Persona3('valentina', 'morano','morano@gmail.com')
console.log(madre);
console.log(madre.telefono); //la propiedad no esta definida
console.log(madre.nombreCompleto());

//diferentes formas de crear objetos
//caso numero 1
let miObjeto = new Object(); //esta es una opcion formal
//caso numero 2
let miObjeto2 = {}; // esta opcion es breve y recomendada

//caso String   
let miCadena1 = new String('Hola'); //Sintaxis formal
//Caso string 2
let miCadena2= 'Hola'; //Esta es la sintaxis simplificada y recomendada

//caso con numeros 1    
let miNumero = new Number(1); //Es formal no recomendable
//Caso con numeros 2
let miNumero2 = 1; //Sintaxis recomendada

//Caso boolean 1
let miBoolean1 = new Boolean(false); // formal
//caso boolean 2 
let miBoolean2 = false; //Sintaxis recomendada

//caso arreglos 1
let miArreglo1 = new Array(); //formal
//caso arreglos 2
let miArreglo2 = []; //Sintaxis recomendada

//caso function 1
let miFuncion1 = new function(){}; //Todo despues de new es considerado objeto
//caso function 2
let miFuncion2 = function(){}; //Notacion simplificada y recomendada
//opciones 2 son simplificadas

//Uso de prototype
Persona3.prototype.telefono = '2604040506';
console.log(padre);
console.log(madre.telefono);
madre.telefono = '5492604040506';
console.log(madre.telefono);

//Uso de call
let persona4 = {
    nombre: 'Kevinzinho',
    apellido: 'castilla',
    nombreCompleto2: function(titulo, telefono){
       return titulo+' '+this.nombre+' '+this.apellido+' '+telefono;
        //return this.nombre+' '+this.apellido;
    }
}
let persona5 ={
    nombre: 'Maxi',
    apellido: 'Zuñiga'
}

console.log(persona4.nombreCompleto2('Lic.', '5492604987654'));
console.log(persona4.nombreCompleto2.call(persona5, 'Ing.', '5492604123456'));

//Metodo Apply
let arreglo = ['Ing.', '5492604566666'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));
