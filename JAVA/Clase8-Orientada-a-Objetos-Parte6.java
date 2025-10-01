/**
 * Clase Persona:
 * Implementa la encapsulación. Los atributos son privados y solo se
 * puede acceder a ellos o modificarlos a través de los métodos públicos
 * (Getters y Setters).
 */
public class Persona {
 
    // 1. Atributos privados
    private String nombre;
    private double sueldo;
    // Se usa 'esElimina' en lugar de 'eliminado' para coincidir con el código del ejercicio.
    private boolean esElimina;
 
    /**
     * Constructor para inicializar todos los atributos.
     */
    public Persona(String nombre, double sueldo, boolean esElimina) {
        this.nombre = nombre;
        this.sueldo = sueldo;
        this.esElimina = esElimina;
    }
 
    // 2. Métodos Getters (para obtener el valor)
    public String getNombre() {
        return this.nombre;
    }
 
    public double getSueldo() {
        return this.sueldo;
    }
 
    // Para booleanos, el Getter típicamente usa 'is'
    public boolean isElimina() {
        return this.esElimina;
    }
 
    // 3. Métodos Setters (para modificar el valor)
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
 
    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
 
    public void setElimina(boolean esElimina) {
        this.esElimina = esElimina;
    }
 
    /**
     * Método opcional para imprimir el estado completo del objeto.
     */
    @Override
    public String toString() {
        return "Persona{nombre='" + nombre + "', sueldo=" + sueldo + ", esElimina=" + esElimina + "}";
    }
}
