// let persona3 = new Persona('Carla', 'Ponce'); esto no se debe hacer: Persona is not defined

class Persona { //Clase padre

    static contadorPersonas = 0; //Atributo estático
    //email = 'valor default email'; //Atributo no estático
    static get MAX_OBJ() {  //Constante estática
        return 5;
    }

  

    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        if(Persona.contadorPersonas < Persona.MAX_OBJ){
            this.idPersona = ++Persona.contadorPersonas;
        } 
        else {
            console.log('Se ha superado el máximo de objetos permitidos: ' + Persona.MAX_OBJ);
        }
        //console.log('Se incrementa el contador: ' + Persona.contadorObjetosPersonas);
        
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
        return this.idPersona + ' ' +  this._nombre + ' ' + this._apellido;
    }

    toString(){
        return this.nombreCompleto();   
    }

    static saludar(){
        console.log('Saludos desde el método static de la clase Persona');
    }

    static saludar2(persona){
        console.log(persona.nombre + ' ' + persona.apellido);
    }
}

class Empleado extends Persona { //Clase hija
    constructor(nombre, apellido, departamento){
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

}

let persona1 = new Persona('Martin', 'Pérez');
console.log(persona1.nombre);
persona1.nombre = 'Juan Carlos';
console.log(persona1.nombre);
//console.log(persona1);

let persona2 = new Persona('Carlos', 'Lara');
console.log(persona2.nombre);
persona2.nombre = 'Maria Laura';
console.log(persona2.nombre);
//console.log(persona2);

let empleado1 = new Empleado('María', 'Gimenez', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombreCompleto());
console.log(empleado1.departamento);

//Object.prototype.toString = function() { Esta es la manera de acceder a atributos y metodos de manera dinamica

console.log(empleado1.toString());
console.log(persona1.toString());

Persona.saludar(); //llamada al método static
Persona.saludar2(persona1); //llamada al método static con parámetro

Empleado.saludar(); //llamada al método static desde la clase hija
Empleado.saludar2(empleado1); //llamada al método static con parámetro desde la clase hija

//console.log(persona1.contadorObjetosPersonas); //undefined, no se accede a atributos estáticos desde objetos
console.log(Persona.contadorObjetosPersonas);
console.log(Empleado.contadorObjetosPersonas);

console.log(empleado1.email); //Atributo no estático
console.log(persona1.email); //Atributo no estático
//console.log(Persona.email); //undefined, no se accede a atributos no estáticos desde la clase

console.log(persona1.toString());
console.log(persona2.toString());
console.log(empleado1.toString());
console.log(Persona.contadorPersonas);
console.log(Empleado.contadorPersonas);
let persona3 = new Persona('Carla', 'Ponce');
console.log(persona3.toString());
console.log(Persona.contadorPersonas);


console.log(Persona.MAX_OBJ);
// Persona.MAX_OBJ = 10; //No se puede modificar una constante
console.log(Persona.MAX_OBJ);


let persona4 = new Persona('Renzo', 'Lopez');
let persona5 = new Persona('Ana', 'Gonzalez');
let persona6 = new Persona('Lucia', 'Martinez');
console.log(Persona.contadorPersonas);
console.log(persona6.toString());
console.log(Persona.MAX_OBJ);
