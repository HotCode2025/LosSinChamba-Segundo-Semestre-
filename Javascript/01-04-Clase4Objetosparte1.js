let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
// Objeto
let persona = {
    nombre: 'kevin',
    apellido : 'castilla',
    email: 'kevinrasgido73@gmail.com',
    edad: 29,
    idioma: 'ES', //ponemos el idioma en español
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


