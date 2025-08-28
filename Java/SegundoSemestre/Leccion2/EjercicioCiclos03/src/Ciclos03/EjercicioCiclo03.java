/*
Ejercicio 3: Leer números hasta que se introduzca un cero
Para cada uno indicar si es par o impar.
Primero lo haremos con la clase Scanner
Luego con la clase JOptionPane
 */
package Ciclos03;

import javax.swing.JOptionPane;

public class EjercicioCiclo03 {

    public static void main(String[] args) {
        int numero;

        do {
            String input = JOptionPane.showInputDialog(null, "Digite un número:");
            if (input == null) {
                break;
            }
            numero = Integer.parseInt(input);

            if (numero != 0) {
                if (numero % 2 == 0) {
                    JOptionPane.showMessageDialog(null, "El número " + numero + " es PAR.");
                } else {
                    JOptionPane.showMessageDialog(null, "El número " + numero + " es IMPAR.");
                }
            }

        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "Programa finalizado. Se ingresó un cero.");
    }
}
