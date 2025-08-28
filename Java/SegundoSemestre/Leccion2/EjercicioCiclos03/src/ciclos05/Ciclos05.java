package Ciclos05;

import javax.swing.JOptionPane;
import java.util.Random;

public class Ciclos05 {

    public static void main(String[] args) {
        
        Random random = new Random();
        
        int numeroSecreto = random.nextInt(101);

        int intento;
        int intentosRealizados = 0;
        
        do {
            
            String entrada = JOptionPane.showInputDialog("Adivina un número entre 0 y 100:");
            intento = Integer.parseInt(entrada);
            intentosRealizados++;
        
            if (intento > numeroSecreto) {
                JOptionPane.showMessageDialog(null, "El número es MENOR.");
            } else if (intento < numeroSecreto) {
                JOptionPane.showMessageDialog(null, "El número es MAYOR.");
            }
        } while (intento != numeroSecreto); 
        
        JOptionPane.showMessageDialog(null, "¡Felicidades! Adivinaste el número correcto: " + numeroSecreto + "\nTe tomó " + intentosRealizados + " intentos.");
    }
}
