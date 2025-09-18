
package clase4;

import java.util.Scanner;

public class Ciclos06 {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;

        do {
            System.out.println("Por favor, ingrese un número (ingrese 0 para salir):");
            numero = entrada.nextInt();
            suma += numero; 
        } while (numero != 0);

        System.out.println("La suma de todos los números introducidos es: " + suma);
        entrada.close();
    }
}