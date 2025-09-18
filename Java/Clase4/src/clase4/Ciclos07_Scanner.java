
package clase4;
import java.util.Scanner;

public class Ciclos07_Scanner {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, elementos = 0, suma = 0;
        float media;

        System.out.println("Ingrese números para calcular la media (ingrese un número negativo para finalizar):");

        do {
            numero = entrada.nextInt();
            if (numero >= 0) {
                suma += numero;
                elementos++;
            }
        } while (numero >= 0);

        if (elementos == 0) {
            System.out.println("No se ingresaron números no negativos.");
        } else {
            media = (float) suma / elementos;
            System.out.println("La media de los números es: " + media);
        }

        entrada.close();
    }
}

