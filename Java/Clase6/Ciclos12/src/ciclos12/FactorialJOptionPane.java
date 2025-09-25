package ciclos12;

import javax.swing.JOptionPane;

public class FactorialJOptionPane {
        public static void main(String[] args) {
        String input;
        int numero;
        long factorial = 1;
       
        input = JOptionPane.showInputDialog("Ingrese un número para calcular su factorial:");
        
        try {
            numero = Integer.parseInt(input); 
 
            if (numero < 0) {
                JOptionPane.showMessageDialog(null, "No se puede calcular el factorial de un número negativo.");
            } else {
                
                for (int i = 1; i <= numero; i++) {
                    factorial *= i;
                }
                JOptionPane.showMessageDialog(null, "El factorial de " + numero + " es: " + factorial);
            }
        } catch (NumberFormatException e) {
           
            JOptionPane.showMessageDialog(null, "Entrada no válida. Por favor, ingrese un número entero.");
        }
    }
}
