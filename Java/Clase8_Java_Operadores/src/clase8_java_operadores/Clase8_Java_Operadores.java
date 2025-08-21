
package clase8_java_operadores;

import java.util.Scanner;

public class Clase8_Java_Operadores {
/*
    
Ejercicio : Rectángulo
Se solicita calcular el área y el perímetro de un rectángulo, 
para esto deberemos crear las variables:
Alto (int)
Ancho(int)
El usuario debe proporcionar los valores de alto, ancho y después 
se debe imprimir el resultado en el siguiente formato: 
    (recuerden no usar acentos, respetar los espacios, mayúsculas, 
    minúsculas y saltos de líneas.
    
Le decimos al usuario:
Digite el alto del rectángulo:
Digite el ancho del rectángulo:

Fórmula:
Área = alto * ancho;
Perímetro = (alto + ancho) * 2;
¿Cuál es el código del ejercicio planteado?
*/
    
    public static void main(String[] args) {
        int alto, ancho;
        Scanner s = new Scanner(System.in);
        System.out.println("Digite el alto del rectangulo: ");
        alto = Integer.parseInt(s.nextLine());
        System.out.println("Digite el ancho del rectangulo:");
        ancho = Integer.parseInt(s.nextLine());
        int area = alto * ancho;
        int perimetro = (alto + ancho) * 2;
        
        System.out.println("El area del rectangulo es: " + area);
        System.out.println("El perimetro del rectangulo es: " + perimetro);
    }
    
}
