/*
Ejercicio 4: Pedir números hasta que se teclee uno negativo,
y mostrar cuántos números se han introducido.
Lo hacemos primero con la clase Scanner
Luego lo hacemos con la clase JOptionPane
 */
package ciclos04;

import javax.swing.JOptionPane;

public class EjercicioCiclos04 {

    public static void main(String[] args) {
        int numero;
        int contador = 0;

        do {
            String input = JOptionPane.showInputDialog(null, "Digite un número (un número negativo para terminar):");
            if (input == null) { // Maneja el caso en que el usuario cancela
                break;
            }
            numero = Integer.parseInt(input);

            if (numero >= 0) {
                contador++; // Incrementa el contador si el número no es negativo
            }

        } while (numero >= 0);

        JOptionPane.showMessageDialog(null, "Se han introducido " + contador + " números.");
    }
}
