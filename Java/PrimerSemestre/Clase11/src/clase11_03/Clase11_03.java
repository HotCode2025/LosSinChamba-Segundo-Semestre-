package clase11_03;
import java.util.Scanner;
public class Clase11_03 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        double num1, num2, resultado;
        System.out.println("Digite numero 1: ");
        num1 = s.nextDouble();
        System.out.println("Digite numero 2: ");
        num2 = s.nextDouble();
        if(num1 == num2){
            resultado = num1 * num2;
        } else if (num1 > num2){
            resultado = num1 - num2;
        } else {
            resultado = num1 + num2;
        }
        System.out.println("El resultado es: " + resultado);
    }
}
