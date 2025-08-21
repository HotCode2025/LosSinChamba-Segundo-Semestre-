
package clase09;
import java.util.Scanner;

public class Clase09_ej05 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float notal, nota2, nota3, suma;
        System.out.println("Digite las tres calificaciones: ");
        notal = Float.parseFloat(entrada.nextLine());
        nota2 = Float.parseFloat(entrada.nextLine());
        nota3 = Float.parseFloat(entrada.nextLine());

        suma = notal + nota2 + nota3;

        System.out.println("\nLa suma es: " + suma);
    }
    
}
