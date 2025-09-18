package clase4;

public class PruebaPersona {
    public static void main(String[] args) {
        Persona persona1 = new Persona();
        persona1.nombre="Gabriel";
        persona1.nombre="Apellido";
        persona1.obtenerInformacion();
        
        Persona persona2 = new Persona();
        System.out.println("Persona2 : " + persona2);
        System.out.println("Persona1 : " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre="Ariel";
        persona2.apellido="Betancud";
        persona2.obtenerInformacion();
        
    }
}
