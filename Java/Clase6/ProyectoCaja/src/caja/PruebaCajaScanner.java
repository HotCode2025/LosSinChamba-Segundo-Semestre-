package caja;
import java.util.Scanner;

public class PruebaCajaScanner {
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Ingrese Alto: "); double alto = scan.nextDouble();
        System.out.println("Ingrese Ancho: "); double ancho = scan.nextDouble();
        System.out.println("Ingrese Profundidad: "); double profundidad = scan.nextDouble();
        Caja c1 = new Caja();
        System.out.println("EL volumen es de la caja es: " + c1.CalcularVolumen(alto, ancho, profundidad));
    }
    
}
