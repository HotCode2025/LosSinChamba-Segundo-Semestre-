class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

let persona1 = new Persona('Leo', 'Messi');
console.log(persona1); // Persona { nombre: 'Leo', apellido: 'Messi' }

let persona2 = new Persona('Cristiano', 'Ronaldo');
console.log(persona2); // Persona { nombre: 'Cristiano', apellido: 'Ronaldo' }
