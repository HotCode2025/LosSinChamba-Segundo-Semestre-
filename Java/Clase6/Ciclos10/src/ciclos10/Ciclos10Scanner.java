package ciclos10;
import java.util.Scanner;

public class Ciclos10Scanner {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int total=0;
        int[] numeros = new int[10];
        for (int i = 0; i < 10; i++) {
            System.out.println("Ingrese el numero " + i + ": ");
            numeros[i] = scan.nextInt();
            total += numeros[i];
        }
        System.out.println("La suma total de los numeros es: " + total);
       
    }
}
