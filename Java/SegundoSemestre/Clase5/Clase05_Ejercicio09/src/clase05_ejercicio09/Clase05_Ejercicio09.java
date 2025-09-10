
package clase05_ejercicio09;

import javax.swing.JOptionPane;


public class Clase05_Ejercicio09 {

    public static void main(String[] args) {
         // Declaramos las variables para el día, mes y año
        int dia, mes, anio;

        // Pedimos los datos al usuario
        dia = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el día:"));
        mes = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el mes:"));
        anio = Integer.parseInt(JOptionPane.showInputDialog("Ingresa el año:"));

        // Validamos la fecha
        if (dia >= 1 && dia <= 30) {
            if (mes >= 1 && mes <= 12) {
                if (anio != 0) { // Un año 0 no es válido
                    JOptionPane.showMessageDialog(null, "La fecha es correcta.");
                } else {
                    JOptionPane.showMessageDialog(null, "La fecha es incorrecta. El año no puede ser 0.");
                }
            } else {
                JOptionPane.showMessageDialog(null, "La fecha es incorrecta. El mes debe estar entre 1 y 12.");
            }
        } else {
            JOptionPane.showMessageDialog(null, "La fecha es incorrecta. El día debe estar entre 1 y 30.");
        }
    }
    
}
