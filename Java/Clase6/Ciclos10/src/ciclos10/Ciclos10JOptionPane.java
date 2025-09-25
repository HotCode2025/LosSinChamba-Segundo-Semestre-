
package ciclos10;
import javax.swing.JOptionPane;

public class Ciclos10JOptionPane {
        public static void main(String[] args) {
        int total=0;
        int[] numeros = new int[10];
        for (int i = 0; i < 10; i++) {
            numeros[i] = Integer.parseInt(JOptionPane.showInputDialog(null, "Ingrese numero: " + i));
            total += numeros[i];
        }
        JOptionPane.showMessageDialog(null, "La suma total de los numeros es: " + total);
    }
}
