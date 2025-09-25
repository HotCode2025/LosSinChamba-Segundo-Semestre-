package caja;

import javax.swing.JOptionPane;

public class PruebaCajaJOptionPane {
    public static void main(String[] args) {
        double alto = Double.parseDouble(JOptionPane.showInputDialog(null, "Ingrese Alto: "));
        double ancho = Double.parseDouble(JOptionPane.showInputDialog(null, "Ingrese Ancho: "));
        double profundidad = Double.parseDouble(JOptionPane.showInputDialog(null, "Ingrese Profundiad: "));
        Caja c1 = new Caja();
        JOptionPane.showMessageDialog(null, "EL volumen es de la caja es: " + c1.CalcularVolumen(alto, ancho, profundidad));
    }
}
