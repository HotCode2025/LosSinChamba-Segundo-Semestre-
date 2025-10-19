package domain;

public class Persona {
    // Atributos privados
    protected String nombre; // -nombre: String
    protected char genero;   // -genero: char
    protected int edad;      // -edad: int
    protected String direccion; // -direccion: String

    // Constructor por defecto
    public Persona() {
    }

    @Override
    public String toString() {
        return "Persona{" + "nombre=" + nombre + ", genero=" + genero + ", edad=" + edad + ", direccion=" + direccion + '}';
    }

    // Constructor con todos los atributos
    public Persona(String nombre, char genero, int edad, String direccion) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
        this.direccion = direccion;
    }

    // Constructor con todos los atributos
    public Persona(String nombre) {
        this.nombre = nombre;
    }
    // Métodos Getters y Setters (según el diagrama)

    // +getNombre(): Str
    public String getNombre() {
        return nombre;
    }

    // +setNombre(String): void
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    // +getGenero(): char
    public char getGenero() {
        return genero;
    }

    // +setGenero(char): void
    public void setGenero(char genero) {
        this.genero = genero;
    }

    // +getEdad(): int
    public int getEdad() {
        return edad;
    }

    // +setEdad(int): void (En el diagrama dice void, pero debería ser setEdad(int edad))
    public void setEdad(int edad) {
        this.edad = edad;
    }

    // +getDireccion(): String
    public String getDireccion() {
        return direccion;
    }

    // +setDireccion(String): void
    public void setDireccion(String direccion) {
        this.direccion = direccion;
    }
}