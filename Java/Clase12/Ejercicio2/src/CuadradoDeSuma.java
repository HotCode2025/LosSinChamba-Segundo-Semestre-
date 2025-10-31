//Ejercicio 2 de la Clase 12
import java.util.Scanner;
import java.lang.Math; // Aunque no es estrictamente necesario, es buena práctica indicar que se usará Math

public class CuadradoDeSuma {

    public static void main(String[] args) {
        // Declaración de variables (usamos double para mayor precisión, aunque se podría usar int o float)
        try (Scanner entrada = new Scanner(System.in)) {
            double a, b;
            double resultadoFormula;
            double resultadoDirecto;
            
// 1. Solicitar la entrada al usuario
            System.out.println("--- Calculo del Cuadrado de una Suma (a+b)^2 ---");
            System.out.print("Ingrese el valor de 'a': ");
            a = entrada.nextDouble();
            System.out.print("Ingrese el valor de 'b': ");
            b = entrada.nextDouble();
            
// 2. Calcular el resultado usando la expansión de la fórmula: a^2 + b^2 + 2*a*b
            resultadoFormula = Math.pow(a, 2) + Math.pow(b, 2) + (2 * a * b);
            // 3. Calcular el resultado usando la forma directa: (a+b)^2
            resultadoDirecto = Math.pow((a + b), 2);
            // 4. Mostrar los resultados
            System.out.println("\n---------------------------------------------------");
            System.out.println("Valores ingresados: a = " + a + ", b = " + b);
            System.out.println("El cuadrado de la suma es (a + b)^2:");
            System.out.println("  Usando la fórmula (a^2 + b^2 + 2ab): " + resultadoFormula);
            System.out.println("  Usando el cálculo directo ((a+b)^2): " + resultadoDirecto);
            System.out.println("---------------------------------------------------");
        }
    }
}