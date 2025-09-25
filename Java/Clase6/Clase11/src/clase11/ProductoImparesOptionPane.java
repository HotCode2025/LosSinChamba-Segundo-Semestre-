
package clase11;

import javax.swing.JOptionPane;

public class ProductoImparesOptionPane {
    public static void main(String[] args) {
        
        long producto = 1; 
        int contador = 0;
        
        for (int i = 1; contador < 10; i++) {
            if (i % 2 != 0) {
                producto *= i;
                contador++;
            }
        }
        
        JOptionPane.showMessageDialog(null, "El producto de los 10 primeros números impares es: " + producto);
    }    
}
