//Ejercico 1 de la Clase 12
import java.util.Scanner;

public class ConversorHoras {

    public static void main(String[] args) {
        // Variables para almacenar los resultados y la entrada
        try ( // Objeto Scanner para leer la entrada del usuario
                Scanner entrada = new Scanner(System.in)) {
            // Variables para almacenar los resultados y la entrada
            int horasTotales;
            int semanas;
            int dias;
            int horasRestantes;
            // Constantes de conversión
            final int HORAS_POR_DIA = 24;
            final int DIAS_POR_SEMANA = 7;
            final int HORAS_POR_SEMANA = HORAS_POR_DIA * DIAS_POR_SEMANA; // 168 horas
            // Solicitar la entrada al usuario
            System.out.print("Ingrese el numero total de horas: ");
            horasTotales = entrada.nextInt();
            
// 1. Calcular el número de semanas
            semanas = horasTotales / HORAS_POR_SEMANA;
           
// 2. Calcular las horas restantes después de restar las semanas
            int horasRestantesDespuesSemanas = horasTotales % HORAS_POR_SEMANA;
            
// 3. Calcular el número de días
            dias = horasRestantesDespuesSemanas / HORAS_POR_DIA;
            
// 4. Calcular las horas restantes finales
            horasRestantes = horasRestantesDespuesSemanas % HORAS_POR_DIA;
            // Mostrar el resultado
            System.out.println("\nEl equivalente de " + horasTotales + " horas es:");
            System.out.println("---------------------------------------------");
            System.out.println("**Semanas:** " + semanas);
            System.out.println("**Dias:** " + dias);
            System.out.println("**Horas:** " + horasRestantes);

        }
    }
}