package clase8_java_operador_ternario;
import java.util.Scanner;
public class Clase8_Java_Operador_ternario {

    /*
     Ejercicio: El mayor de 2 números
     Usaremos el Operador Ternario
     Le vamos a pedir los números al usuario
     */
    public static void main(String[] args) {
        int a, b;
        Scanner s = new Scanner(System.in);
        System.out.println("Digite el numero A: ");
        a = Integer.parseInt(s.nextLine());
        System.out.println("Digite el numero B: ");
        b = Integer.parseInt(s.nextLine());
        int mayor = a>b ? a : b;
        System.out.println("El numero mayor es: " + mayor );
        
    }
    
}
