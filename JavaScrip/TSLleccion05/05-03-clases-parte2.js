//let persona3 = new Persona('Ana', 'García');



class Persona{ //Clase Padre
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
    nombreCompleto(){
    return this._nombre + ' ' + this._apellido;
}
//Sobreescribiendo el método de la clase padre (Object)
toString(){ //Regresa un String
    //Se aplica el polimorfismo que significa = multiples formas en tiempo de ejecución
    //El método que se ejecuta depende si es una referencia de tipo padre o hija
    return this.nombreCompleto();
}

class Empleado extends Persona{ //Clase Hija
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
    //Sobreescritura
nombreCompleto(){
    return super.nombreCompleto() + ', ' + this._departamento;

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
console.log(empleado1);  // Empleado { _nombre: 'Lola', _apellido: 'Ruiz', _departamento: 'Sistemas' }
console.log(empleado1.nombreCompleto); // Lola Ruiz, Sistemas

//Object.prototype.toString Esta es la manera de acceder a atributos y métodos de manera dinámica
console.log(empleado1.toString());   // Lola Ruiz, Sistemas
console.log(persona1.toString());   // Juan Carlos Perez


