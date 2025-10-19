//Proyecto Ventas Tarea 10 - Manejo de clases y objetos en TypeScript
class Producto {
  
    idProducto;     
    nombre;         
    precio;         
    
   
    static contadorProductos = 0;

    constructor(nombre, precio) {
        Producto.contadorProductos++;
        this.idProducto = Producto.contadorProductos;
        
        this.nombre = nombre;
        this.precio = precio;
    }

  
    getIdProducto() { return this.idProducto; }
    getNombre() { return this.nombre; }
    getPrecio() { return this.precio; }

  
    setNombre(nombre) { this.nombre = nombre; }
    setPrecio(precio) { this.precio = precio; }

    toString() {
        return `[ID: ${this.idProducto}] ${this.nombre} - $${this.precio.toFixed(2)}`;
    }
}


class Orden {
    
    idOrden;                        
    productos = [];                 
    contadorProductosAgregados = 0; 
    
   
    static MAX_PRODUCTOS = 5;

    
    static contadorOrdenes = 0;

    constructor() {
        Orden.contadorOrdenes++;
        this.idOrden = Orden.contadorOrdenes;
    }

  
    agregarProducto(producto) {
        if (this.contadorProductosAgregados < Orden.MAX_PRODUCTOS) {
            this.productos.push(producto);
            this.contadorProductosAgregados++;
            return true;
        } else {

            console.log(`Límite alcanzado: No se pudo agregar ${producto.getNombre()}. Orden #${this.idOrden} ya tiene ${Orden.MAX_PRODUCTOS} productos.`);
            return false;
        }
    }

   
    calcularTotal() {
        return this.productos.reduce((total, producto) => total + producto.getPrecio(), 0);
    }


    mostrarOrden() {
        const total = this.calcularTotal();
        
        console.log(`\n============================================`);
        console.log(`ORDEN #${this.idOrden}`);
        console.log(`Productos: ${this.contadorProductosAgregados} / ${Orden.MAX_PRODUCTOS}`);
        console.log(`--------------------------------------------`);
        
        this.productos.forEach(producto => {
            console.log(`  - ${producto.toString()}`);
        });
        
        console.log(`--------------------------------------------`);
        console.log(` TOTAL: $${total.toFixed(2)}`);
        console.log(`============================================`);
    }
}



console.log("--- Creando Productos Alimenticios (12 en total) ---");

const prod1 = new Producto("Pan Integral (600g)", 3.50);
const prod2 = new Producto("Leche Entera (Litro)", 1.99);
const prod3 = new Producto("Huevos (Docena)", 4.25);
const prod4 = new Producto("Queso Fresco (250g)", 5.70);
const prod5 = new Producto("Tomates Perita (kg)", 2.10);
const prod6 = new Producto("Cebollas (kg)", 1.50);
const prod7 = new Producto("Pollo (kg)", 9.80);
const prod8 = new Producto("Arroz Blanco (1kg)", 2.40);
const prod9 = new Producto("Fideos Espagueti", 1.20);
const prod10 = new Producto("Aceite de Girasol (Litro)", 6.90);
const prod11 = new Producto("Palta (unidad)", 1.75);
const prod12 = new Producto("Salmón (Filete)", 15.00);


// --- 2. Creación y llenado de la primera orden (Orden #1) ---
console.log("\n--- Creando Orden #1 (Compra con límite) ---");
const orden1 = new Orden(); 

orden1.agregarProducto(prod1); // 1. Pan
orden1.agregarProducto(prod2); // 2. Leche
orden1.agregarProducto(prod3); // 3. Huevos
orden1.agregarProducto(prod4); // 4. Queso
orden1.agregarProducto(prod5); // 5. Tomates (Límite alcanzado)

// Intento de agregar un sexto producto (debe ser bloqueado)
orden1.agregarProducto(prod6); 

orden1.mostrarOrden();


// --- 3. Creación y llenado de la segunda orden (Orden #2) ---
console.log("\n--- Creando Orden #2 (Otra compra) ---");
const orden2 = new Orden(); 

orden2.agregarProducto(prod7); // 1. Pollo
orden2.agregarProducto(prod8); // 2. Arroz
orden2.agregarProducto(prod9); // 3. Fideos
orden2.agregarProducto(prod10);// 4. Aceite
orden2.agregarProducto(prod11);// 5. Aguacates (Límite alcanzado)

// Intento de agregar un sexto producto (debe ser bloqueado)
orden2.agregarProducto(prod12);

orden2.mostrarOrden();