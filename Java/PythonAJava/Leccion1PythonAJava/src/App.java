import java.util.*;
import java.time.*;

public class App {
    private static final Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        while (true) {
            System.out.println("\n===== MENÚ DEMOS (Python → Java) =====");
            System.out.println("1) Variables, reasignación y \"id\"/type");
            System.out.println("2) Tipos básicos (int, double, String, boolean)");
            System.out.println("3) Cadenas: concatenación y casteo String→int");
            System.out.println("4) Booleanos y if/else");
            System.out.println("5) Suma leyendo 2 números (input)");
            System.out.println("6) Operadores aritméticos (+-*/ // % **)");
            System.out.println("7) Área y perímetro de rectángulo");
            System.out.println("8) Operadores de asignación (+= -= *= /=)");
            System.out.println("9) Operadores de comparación (== != > <= >=)");
            System.out.println("10) Par o impar");
            System.out.println("11) Mayor de edad");
            System.out.println("12) Operadores lógicos (and/or/not)");
            System.out.println("13) Valor dentro de rango [0..5]");
            System.out.println("14) Vacaciones o día de descanso (or/not)");
            System.out.println("15) Rango de 20 a 30 años");
            System.out.println("16) Mayor de dos números");
            System.out.println("17) Tienda de libros");
            System.out.println("0) Salir");
            System.out.print("Elegí una opción: ");

            String in = sc.nextLine().trim();
            if (in.equals("0")) break;

            try {
                switch (Integer.parseInt(in)) {
                    case 1 -> demoVariablesYIdYType();
                    case 2 -> demoTiposBasicos();
                    case 3 -> demoCadenasYCasteo();
                    case 4 -> demoBooleanosYIf();
                    case 5 -> demoSumaConInput();
                    case 6 -> demoOperadoresAritmeticos();
                    case 7 -> demoRectangulo();
                    case 8 -> demoAsignacion();
                    case 9 -> demoComparacion();
                    case 10 -> demoParImpar();
                    case 11 -> demoMayorEdad();
                    case 12 -> demoLogicos();
                    case 13 -> demoRango05();
                    case 14 -> demoVacacionesODescanso();
                    case 15 -> demoRango20a30();
                    case 16 -> demoMayorDeDos();
                    case 17 -> tiendaLibros();
                    default -> System.out.println("Opción inválida.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Ingresá un número de menú válido.");
            }
        }
        System.out.println("¡Listo!");
    }

    // 1) Variables, reasignación y “id”/type
    static void demoVariablesYIdYType() {
        Object miVariable = 3;                 // int (boxed)
        System.out.println(miVariable);
        miVariable = "Hola a todos";           // String
        System.out.println(miVariable);
        miVariable = 3.5;                      // double (boxed)
        System.out.println(miVariable);

        Integer x = 10, y = 2;
        Integer z = x + y;

        // Aproximación a id(obj): identityHashCode (no es dirección real de memoria)
        System.out.println(System.identityHashCode(x));
        System.out.println(System.identityHashCode(y));
        System.out.println(System.identityHashCode(z));
        System.out.println(System.identityHashCode(miVariable));

        String a = "Hola a todos";
        System.out.println(a.getClass());      // tipo en runtime

        Object a2 = Boolean.FALSE;
        System.out.println(a2.getClass());
    }

    // 2) Tipos básicos
    static void demoTiposBasicos() {
        int x = 10;
        System.out.println(x);
        System.out.println(((Object)x).getClass()); // boxing para ver clase

        double d = 14.5;
        System.out.println(d);
        System.out.println(((Object)d).getClass());

        String s = "Hola Mundo";
        System.out.println(s);
        System.out.println(s.getClass());

        boolean b = true;
        System.out.println(b);
        System.out.println(((Object)b).getClass());
    }

    // 3) Cadenas y casteo
    static void demoCadenasYCasteo() {
        String miGrupoFavorito = "Red Hot Chili Peppers:";
        String caracteristicas = " Banda de Rock";
        System.out.println("Mi grupo favorito es: " + miGrupoFavorito + caracteristicas);

        String numero1 = "7";
        String numero2 = "8";
        int suma = Integer.parseInt(numero1) + Integer.parseInt(numero2);
        System.out.println(suma);
    }

    // 4) Booleanos y if/else
    static void demoBooleanosYIf() {
        boolean miBooleano = true;
        System.out.println(miBooleano);
        miBooleano = 3 > 2;
        System.out.println(miBooleano);

        if (miBooleano) {
            System.out.println("El resultado es Verdadero");
        } else {
            System.out.println("El resultado es Falso");
        }
    }

    // 5) Suma con input (dos enteros)
    static void demoSumaConInput() {
        System.out.print("Escribe el primer número: ");
        int n1 = Integer.parseInt(sc.nextLine());
        System.out.print("Escribe el segundo número: ");
        int n2 = Integer.parseInt(sc.nextLine());
        System.out.println("El resultado de la suma es: " + (n1 + n2));
    }

    // 6) Operadores aritméticos
    static void demoOperadoresAritmeticos() {
        int A = 8, B = 5;
        int suma = A + B;
        System.out.println("Resultado de la suma " + suma);
        System.out.printf("El resultado de la suma es: %d%n", suma);

        int resta = A - B;
        System.out.printf("El resultado de la resta es: %d%n", resta);

        int multiplicacion = A * B;
        System.out.printf("El resultado de la multiplicación es: %d%n", multiplicacion);

        double division = (double) A / B; // división real
        System.out.printf("El resultado de la división es: %.4f%n", division);

        int divisionEntera = A / B;       // división entera
        System.out.printf("El resultado de la división (int) es: %d%n", divisionEntera);

        int modulo = A % B;
        System.out.printf("El residuo (módulo) es: %d%n", modulo);

        double exponente = Math.pow(A, B);
        System.out.printf("El resultado del exponente es: %.0f%n", exponente);
    }

    // 7) Área y perímetro de rectángulo
    static void demoRectangulo() {
        System.out.print("Proporciona el alto del rectángulo: ");
        int alto = Integer.parseInt(sc.nextLine());
        System.out.print("Proporciona el ancho del rectángulo: ");
        int ancho = Integer.parseInt(sc.nextLine());
        int area = alto * ancho;
        int perimetro = (alto + ancho) * 2;
        System.out.println("Área: " + area);
        System.out.println("Perímetro: " + perimetro);
    }

    // 8) Operadores de asignación
    static void demoAsignacion() {
        int miVariable3 = 10;
        System.out.println(miVariable3);

        miVariable3 = miVariable3 + 1;
        System.out.println(miVariable3);

        miVariable3 += 1;
        System.out.println(miVariable3);

        miVariable3 -= 2;
        System.out.println(miVariable3);

        miVariable3 *= 3;
        System.out.println(miVariable3);

        miVariable3 /= 2;
        System.out.println(miVariable3);
    }

    // 9) Comparación
    static void demoComparacion() {
        int d = 4, b = 2;
        boolean r;

        r = d == b;
        System.out.println("== " + r);

        r = d != b;
        System.out.println("!= " + r);

        r = d > b;
        System.out.println("> " + r);

        r = d <= b;
        System.out.println("<= " + r);

        r = d >= b;
        System.out.println(">= " + r);
    }

    // 10) Par / Impar
    static void demoParImpar() {
        System.out.print("Digite un número: ");
        int a = Integer.parseInt(sc.nextLine());
        int residuo = a % 2;
        System.out.println("Residuo: " + residuo);
        if (residuo == 0) {
            System.out.printf("El valor de a es: %d y es PAR%n", a);
        } else {
            System.out.printf("El valor de a es: %d y es IMPAR%n", a);
        }
    }

    // 11) Mayor de edad
    static void demoMayorEdad() {
        final int edadAdulto = 18;
        System.out.print("Digite su edad: ");
        int edad = Integer.parseInt(sc.nextLine());
        if (edad >= edadAdulto) {
            System.out.printf("Su edad es: %d años, usted es mayor de edad%n", edad);
        } else {
            System.out.printf("Su edad es: %d años, usted es menor de edad%n", edad);
        }
    }

    // 12) Lógicos
    static void demoLogicos() {
        boolean a = false;
        boolean b = true;

        boolean resultado = a && b;
        System.out.println("a AND b = " + resultado);

        resultado = a || b;
        System.out.println("a OR b  = " + resultado);

        resultado = !a;
        System.out.println("NOT a   = " + resultado);
    }

    // 13) Rango 0..5
    static void demoRango05() {
        System.out.print("Digite un número dentro del rango 0 al 5: ");
        int valor = Integer.parseInt(sc.nextLine());
        int min = 0, max = 5;
        boolean dentro = (valor >= min && valor <= max);
        if (dentro) {
            System.out.printf("El valor %d está dentro del rango%n", valor);
        } else {
            System.out.printf("El valor %d NO está dentro del rango%n", valor);
        }
    }

    // 14) Vacaciones o día de descanso
    static void demoVacacionesODescanso() {
        boolean vacaciones = false;
        boolean diaDescanso = true;

        if (!(vacaciones || diaDescanso)) {
            System.out.println("Tiene trabajo que hacer");
        } else {
            System.out.println("Puede asistir al juego");
        }
    }

    // 15) Rango 20..30 (como en el ejemplo)
    static void demoRango20a30() {
        System.out.print("Digite su edad: ");
        int edad = Integer.parseInt(sc.nextLine());

        boolean veinte = edad >= 20 && edad < 30;
        boolean treinta = edad >= 30 && edad < 40;

        if (veinte || treinta) {
            if (veinte) {
                System.out.println("Estás dentro del rango de los 20's");
            } else if (treinta) {
                System.out.println("Estás dentro del rango de los 30's");
            }
        } else {
            System.out.println("No está dentro del rango de 20 a 30 (extendido a 40 como en el ejemplo).");
        }
    }

    // 16) Mayor de dos números
    static void demoMayorDeDos() {
        System.out.print("Digite el valor para el número 1: ");
        int n1 = Integer.parseInt(sc.nextLine());
        System.out.print("Digite el valor para el número 2: ");
        int n2 = Integer.parseInt(sc.nextLine());

        if (n1 > n2) {
            System.out.println("El número 1 es mayor");
        } else if (n1 < n2) {
            System.out.println("El número 2 es mayor");
        } else {
            System.out.println("Son iguales");
        }
    }

    // 17) Tienda de libros
    static void tiendaLibros() {
        System.out.println("Digite los siguientes datos del libro");
        System.out.print("Digite el nombre del Libro: ");
        String nombre = sc.nextLine();

        System.out.print("Digite el ID del Libro: ");
        int id = Integer.parseInt(sc.nextLine());

        System.out.print("Digite el precio del Libro: ");
        double precio = Double.parseDouble(sc.nextLine());

        System.out.print("Indicar si el envío es gratuito (True/False): ");
        String envioStr = sc.nextLine();

        Object envioGratuito;
        if (envioStr.equalsIgnoreCase("True")) {
            envioGratuito = true;
        } else if (envioStr.equalsIgnoreCase("False")) {
            envioGratuito = false;
        } else {
            envioGratuito = "El valor es incorrecto, debe escribir True/False";
        }

        System.out.println("\n----- Información del Libro -----");
        System.out.println("Nombre: " + nombre);
        System.out.println("Id: " + id);
        System.out.println("Precio: " + precio);
        System.out.println("Envío Gratuito?: " + envioGratuito);
    }
}
