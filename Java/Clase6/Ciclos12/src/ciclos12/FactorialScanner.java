package ciclos12;
import java.util.Scanner;

public class FactorialScanner {
        public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        long factorial = 1;
 
        System.out.print("Ingrese un número para calcular su factorial: ");
        numero = entrada.nextInt();
 
        
        if (numero < 0) {
            System.out.println("No se puede calcular el factorial de un número negativo.");
        } else {
           
            for (int i = 1; i <= numero; i++) {
                factorial *= i;
            }
            System.out.println("El factorial de " + numero + " es: " + factorial);
        }
        
        entrada.close(); 
    }
}
