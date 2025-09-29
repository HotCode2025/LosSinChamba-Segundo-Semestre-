//let persona3 = new Persona('Ana', 'García');


class Persona{ //Clase padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
}

class Empleado extends Persona{ //Clase hija
    constructo(nombre, apellido, departamento){
        super(nombre, apellido);
        this._departamento = departamento;
    }

    get departamento(){
        return this._departamento;
    }

    set departamento(departamento){
        this._departamento = departamento;
    }
}


let persona1 = new Persona('Leo', 'Messi');
console.log(persona1.nombre); //Leo
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);   // Juan Carlos
//console.log(persona1);

let persona2 = new Persona('Cristiano', 'Ronaldo');
console.log(persona2.nombre); //Cristiano
persona2.nombre = 'María Laura';
console.log(persona2.nombre);   // María Laura
//console.log(persona2);

let Empleado = new Empleado('Lola', 'Ruiz', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);
