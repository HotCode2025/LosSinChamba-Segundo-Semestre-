import java.util.Scanner;

public class App {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        // Solicita el título del libro
        System.out.println("Proporciona el título:");
        String titulo = sc.nextLine();

        // Solicita el autor del libro
        System.out.println("Proporciona el autor:");
        String autor = sc.nextLine();

        // Imprime la información en el formato solicitado
        System.out.println(titulo + " fue escrito por " + autor);

        sc.close(); // Cierra el Scanner (buena práctica)
    }
}
