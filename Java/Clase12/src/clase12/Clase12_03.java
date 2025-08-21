package clase12;

import java.util.Scanner;
/*Ejercicio 3: La calificacion final de un estudiante de informática

se calcula con base a las calificaciones de cuatro aspectos de su

rendimiento académico: participación, primer examen parcial, segundo

examen parcial y examen final. Sabiendo que las calificaciones anteriores

entran a la calificación final con ponderaciones de 10%, 25%, 25%

y 40%, Hacer un programa que calcule e imprima la calificación final

obtenida por un estudiante. 

Que el usuario digite las calificaciones de estos 4 datos y así podremos tener,

la calificación final.


*/

public class Clase12_03 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Ingrese la calificacion de Participacion (0-100): ");
        double participacion = s.nextDouble();
        System.out.print("Ingrese la calificacion del Primer Examen Parcial (0-100): ");
        double primerParcial = s.nextDouble();
        System.out.print("Ingrese la calificacion del Segundo Examen Parcial (0-100): ");
        double segundoParcial = s.nextDouble();
        System.out.print("Ingrese la calificacion del Examen Final (0-100): ");
        double examenFinal = s.nextDouble();
        double porcentajeParticipacion = 0.10;
        double porcentajePrimerParcial = 0.25;
        double porcentajeSegundoParcial = 0.25;
        double porcentajeExamenFinal = 0.40;
        double gradoParticipacion = participacion * porcentajeParticipacion;
        double gradoPrimerParcial = primerParcial * porcentajePrimerParcial;
        double gradoSegundoParcial = segundoParcial * porcentajeSegundoParcial;
        double gradoExamenFinal = examenFinal * porcentajeExamenFinal;
        double finalGrado = gradoParticipacion + gradoPrimerParcial + gradoSegundoParcial + gradoExamenFinal;
        System.out.println("\n--- Resumen de Calificaciones ---");
        System.out.println("Calificacion de Participacion (10%): " + participacion);
        System.out.println("Calificacion Primer Parcial (25%): " + primerParcial);
        System.out.println("Calificacion Segundo Parcial (25%): " + segundoParcial);
        System.out.println("Calificacion Examen Final (40%): " + examenFinal);
        System.out.println("---------------------------------");
        System.out.printf("La CALIFICACION FINAL del estudiante es: %.2f%n", finalGrado); // %.2f formats to two decimal places
        s.close();
    }
    
}
