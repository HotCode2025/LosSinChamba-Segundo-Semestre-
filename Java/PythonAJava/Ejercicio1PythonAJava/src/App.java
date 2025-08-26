import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            try {
                // Solicitar la calificación al usuario
                System.out.print("¿Cómo estuvo tu día? Califica del 1 al 10: ");
                String calificacionStr = sc.nextLine();
                int calificacion = Integer.parseInt(calificacionStr);

                // Validar que la calificación esté en el rango de 1 a 10
                if (calificacion >= 1 && calificacion <= 10) {
                    System.out.println("¡Entendido! Tu día estuvo de: " + calificacion + ".");
                    if (calificacion >= 8) {
                        System.out.println("¡Me alegra saber que tuviste un gran día!");
                    } else if (calificacion >= 5) {
                        System.out.println("Espero que mañana sea aún mejor.");
                    } else {
                        System.out.println("Lamento escuchar eso. ¡Espero que las cosas mejoren pronto!");
                    }
                    break; // salir del bucle si la calificación es válida
                } else {
                    System.out.println("Por favor, introduce un número entre 1 y 10.");
                }

            } catch (NumberFormatException e) {
                // Manejar el error si el usuario no introduce un número
                System.out.println("Entrada no válida. Por favor, introduce un número entero.");
            }
        }

        sc.close();
    }
}
