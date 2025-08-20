package clase12;
import java.util.Scanner;
public class Clase12_01 {
/*

Ejercicio 1: Construir un programa que, dado un número total de

horas, devuelve el número de semanas, días y horas equivalentes.

Por ejemplo dado un total de 1000 horas debe mostrar 5 semanas,

6 días y 16 horas.


 */
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.print("Ingrese el numero total de horas: ");
        int totalHoras = s.nextInt();

        int semanas = totalHoras / (7 * 24);
        int restante = totalHoras % (7 * 24);
        
        int dias = restante / 24;
        int horas = restante % 24;

        System.out.print(totalHoras + " horas equivalen a: ");
        System.out.print(semanas + " semanas, ");
        System.out.print(dias + " dias, y ");
        System.out.print(horas + " horas. ");

        s.close();
    }
    
}
