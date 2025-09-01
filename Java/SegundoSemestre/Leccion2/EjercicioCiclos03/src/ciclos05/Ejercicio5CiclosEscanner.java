package ciclos05;


import java.util.Scanner;
import java.util.Random;

public class Ejercicio5CiclosEscanner {

    public static void main(String[] args) {

        try (Scanner entrada = new Scanner(System.in)) {

            Random aleatorio = new Random();

            int numeroAleatorio = aleatorio.nextInt(101);
            int numeroUsuario;
            int intentos = 0;
            boolean adivinado = false;

            do {
                System.out.print("Adivina el número (entre 0 y 100): ");
                numeroUsuario = entrada.nextInt();
                intentos++;

                if (numeroUsuario > numeroAleatorio) {
                    System.out.println("Es menor");
                } else if (numeroUsuario < numeroAleatorio) {
                    System.out.println("Es mayor");
                } else {
                    adivinado = true;
                    System.out.println("¡Felicidades! Adivinaste el número.");
                }
            } while (!adivinado);
            System.out.println("El número de intentos fue: " + intentos);

        }
    }
}
