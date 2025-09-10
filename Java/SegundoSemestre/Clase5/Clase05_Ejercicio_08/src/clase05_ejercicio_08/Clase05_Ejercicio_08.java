package clase05_ejercicio_08;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class Clase05_Ejercicio_08 {

    public static void main(String[] args) {

    Scanner scan = new Scanner(System.in);
        System.out.println("Ingrese un numero: ");
        int num = scan.nextInt();
        
        List<String> listaNumeros = new ArrayList();
        
        for (int i = 0; i < num; i++) {
            listaNumeros.add(String.valueOf(i));
        }
        
        JOptionPane.showMessageDialog(null, listaNumeros.toString());
        
    }
}
