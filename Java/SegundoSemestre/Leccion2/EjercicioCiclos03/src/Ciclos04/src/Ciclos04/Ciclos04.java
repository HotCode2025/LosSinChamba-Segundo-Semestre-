/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
*/
package Ciclos04;

import java.util.Scanner;
    

public class Ciclos04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        int contador = 0;

        System.out.println("Digite un número (un número negativo para terminar): ");
        numero = entrada.nextInt();

        while (numero >= 0) {
            contador++; // Incrementa el contador por cada número positivo o cero
            System.out.println("Digite otro número (un número negativo para terminar): ");
            numero = entrada.nextInt();
        }

        System.out.println("Se han introducido " + contador + " números.");
    }
}

