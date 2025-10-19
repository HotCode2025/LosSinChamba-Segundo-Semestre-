class Persona {
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }
    get idPersona(){
        return this._idPersona;
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
    get edad(){
        return this._edad;
    }
    set edad(edad){
        this._edad = edad;
    }
    toString(){
        return 
        `ID: ${this._idPersona}, 
        Nombre: ${this._nombre}, 
        Apellido: ${this._apellido}, 
        Edad: ${this._edad}`;
    }

}

class Empleado extends Persona {
    static contadorEmpleados = 0;
    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._sueldo = sueldo;
    }           
    get idEmpleado(){
        return this._idEmpleado;
    }
    get sueldo(){
        return this._sueldo;
    }
    set sueldo(sueldo){
        this._sueldo = sueldo;
    }
    toString(){
        return `${super.toString()},
        ID Empleado: ${this._idEmpleado},
        Sueldo: ${this._sueldo}`;
    }
}

class Cliente extends Persona {
    static contadorClientes = 0;
    constructor(nombre, apellido, edad, fechaRegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadorClientes;
        this._fechaRegistro = fechaRegistro;
    }
    get idCliente(){
        return this._idCliente;
    }
    get fechaRegistro(){
        return this._fechaRegistro;
    }
    set fechaRegistro(fechaRegistro){
        this._fechaRegistro = fechaRegistro;
    }
    toString(){
        return `${super.toString()},
        ID Cliente: ${this._idCliente},
        Fecha de Registro: ${this._fechaRegistro}`;
    }
}
// Pruebas de las clases/Empleado/Cliente

let persona1 = new Persona('Juan', 'Pérez', 30);
console.log(persona1.toString());
let empleado1 = new Empleado('Ana', 'García', 28, 50000);
console.log(empleado1.toString());
let cliente1 = new Cliente('Luis', 'Martínez', 35, new Date());
console.log(cliente1.toString());


let persona2 = new Persona('María', 'López', 25);
console.log(persona2.toString());
let empleado2 = new Empleado('Carlos', 'Lopez', 40, 60000);
console.log(empleado2.toString());
let cliente2 = new Cliente('Sofía', 'Hernández', 32, new Date());
console.log(cliente2.toString());

