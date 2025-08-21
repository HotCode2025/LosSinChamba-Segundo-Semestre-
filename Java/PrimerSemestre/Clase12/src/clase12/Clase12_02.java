package clase12;
import java.util.Scanner;
/*

Ejercicio 2: Hacer un programa que calcule el cuadro de una suma,

el usuario debe ingresar el valor de a y el valor de b.

Formula: (a+b)2=a2+b2+2*a*b

Para esto deberán utilizar la clase Math y un método llamado pow


 */
public class Clase12_02 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Ingrese el valor de a: ");
        double a = s.nextDouble();
        System.out.print("Ingrese el valor de b: ");
        double b = s.nextDouble();
        double aCuadrado = Math.pow(a, 2);
        double bCuadrado = Math.pow(b, 2);
        double dosAB = 2 * a * b;
        double resultadoFormula = aCuadrado + bCuadrado + dosAB;
        double sumaAB = a + b;
        double resultadoDirecto = Math.pow(sumaAB, 2);
        System.out.println("\nCalculando (a+b)^2:");
        System.out.println("Usando la formula (a^2 + b^2 + 2*a*b): " + resultadoFormula);
        System.out.println("Verificacion directa ((a+b)^2): " + resultadoDirecto);
        s.close();
    }
    
}
