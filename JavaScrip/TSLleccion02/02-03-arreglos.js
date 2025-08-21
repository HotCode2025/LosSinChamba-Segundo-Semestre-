// VIDEO 1
//let autos = new Array('BMW', 'Mercedes Benz', 'Volvo', 'Audi');
let autos = ['BMW', 'Mercedes Benz', 'Volvo', 'Audi'];
console.log(autos); [ 'BMW', 'Mercedes Benz', 'Volvo', 'Audi' ]

// VIDEO 2
console.log(autos[0]); // BMW
console.log(autos[2]); // Mercedes Benz

for(let i = 0; i < autos.length; i++) {
    console.log(i + ' : ' + autos[i]);
} // 0: BMW, 1: Mercedes Benz, 2: Volvo, 3: Audi

//VIDEO 3
//Modificar un elemento del arreglo
autos[1] = 'Mercedes';
console.log(autos[1]); Mercedes

//arreglamos nuevos valores al arreglo
autos.push('FORD');
console.log(autos); // [ 'BMW', 'Mercedes', 'Volvo', 'Audi', 'Audi' ]

//Otra forma de agregar un elemento al final del arreglo
autos[autos.length] = 'Chevrolet';
console.log(autos); // [ 'BMW', 'Mercedes', 'Volvo', 'Audi

//Tercera forma de agregar elementos teniendo cuidado 
auto[6] = 'Toyota';
console.log(autos); // [ 'BMW', 'Mercedes', 'Volvo', 'Audi


//VIDEO 4
//Como pregunatr si es un array o arreglo
console.log(Array.isArray(autos)); // true

console.log(autos instanceof Array); // true