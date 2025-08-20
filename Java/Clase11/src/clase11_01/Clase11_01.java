package clase11_01;

import java.util.Scanner;

public class Clase11_01 {
    public static void main(String[] args) {
        double nota1, nota2, nota3, promedio;
        Scanner s = new Scanner(System.in);
        System.out.println("Ingrese la nota 1: ");
        nota1 = s.nextDouble();
        System.out.println("Ingrese la nota 2: ");
        nota2 = s.nextDouble();
        System.out.println("Ingrese la nota 3: ");
        nota3 = s.nextDouble();
        promedio = (nota1 + nota2 + nota3) / 3;
        if (promedio > 70) System.out.println("El alumno esta aprobado: " + promedio);
        else System.out.println("El alumno esta desaprobado: " + promedio);
        
    }
    
    
}
