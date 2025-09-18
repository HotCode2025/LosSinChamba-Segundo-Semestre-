package clase4;
import javax.swing.JOptionPane;
public class Ciclos07JOptionPane {

    public static void main(String[] args) {
        int numero, elementos = 0, suma = 0;
        float media;

        do {
            String input = JOptionPane.showInputDialog("Digite un número (negativo para finalizar):");
            numero = Integer.parseInt(input);

            if (numero >= 0) {
                suma += numero;
                elementos++;
            }
        } while (numero >= 0);

        if (elementos == 0) {
            JOptionPane.showMessageDialog(null, "No se ingresaron números no negativos.");
        } else {
            media = (float) suma / elementos;
            JOptionPane.showMessageDialog(null, "La media de los números es: " + media);
        }
    }
}

