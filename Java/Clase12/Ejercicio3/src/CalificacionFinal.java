//Ejercicio3
import java.util.Scanner;

public class CalificacionFinal {

    public static void main(String[] args) {
        // Variables para almacenar las calificaciones ingresadas por el usuario
        try (Scanner entrada = new Scanner(System.in)) {
            double participacion, primerParcial, segundoParcial, examenFinal;
            // Variable para almacenar el resultado final
            double calificacionFinal;
            // 1. Solicitar la entrada de las calificaciones
            System.out.println("--- Calculo de Calificacion Final Ponderada ---");
            System.out.print("Ingrese la calificacion de Participacion (10%): ");
            participacion = entrada.nextDouble();
            System.out.print("Ingrese la calificacion del Primer Examen Parcial (25%): ");
            primerParcial = entrada.nextDouble();
            System.out.print("Ingrese la calificacion del Segundo Examen Parcial (25%): ");
            segundoParcial = entrada.nextDouble();
            System.out.print("Ingrese la calificacion del Examen Final (40%): ");
            examenFinal = entrada.nextDouble();
            
// 2. Calcular la calificación final aplicando las ponderaciones
            calificacionFinal = (participacion * 0.10) +
                    (primerParcial * 0.25) +
                    (segundoParcial * 0.25) +
                    (examenFinal * 0.40);
            
// 3. Mostrar el resultado
            System.out.println("\n---------------------------------------------------");
            System.out.printf("La Calificacion Final Ponderada del estudiante es: %.2f\n", calificacionFinal);
            System.out.println("---------------------------------------------------");
        }
    }
}