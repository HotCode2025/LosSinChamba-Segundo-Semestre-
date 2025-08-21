package clase11_02;
import java.util.Scanner;
public class Clase11_02 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        double compra, descuento, precio_final;
        System.out.println("Digite la cantidad a pagar: ");
        compra = s.nextDouble();
        if(compra > 100) {
            descuento = compra * 0.2;
        }
        else {
            descuento = 0;
        }
        precio_final = compra - descuento;
        System.out.println("El precio a pagar es: " + precio_final);
    }
}
