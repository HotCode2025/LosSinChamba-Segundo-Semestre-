package clase3;
import java.util.Scanner;

public class Clase3 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String nombreLibro, nombreAutor;
        System.out.println("Ingrese el nombre del libro: ");
        nombreLibro = s.nextLine();
        System.out.println("Ingrese el autor del libro: ");
        nombreAutor = s.nextLine();
        System.out.println(nombreLibro + " fue escrito por  " + nombreAutor);
    }
}
