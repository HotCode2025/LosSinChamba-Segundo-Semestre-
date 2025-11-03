package com.biblioteca.main;

import com.biblioteca.modelo.Libro;
import com.biblioteca.modelo.Usuario;
import com.biblioteca.controlador.Biblioteca;
import java.util.Scanner;

/**
 * Proyecto Integrador - Sistema de Gestión de Biblioteca
 * 2º Semestre Los Sin Chamba
 * 
 * Sistema completo de gestión de biblioteca con:
 * - Menú interactivo
 * - Programación Orientada a Objetos
 * - Bucles y Condicionales
 * - Manejo de colecciones
 * 
 * @author Los Sin Chamba
 * @version 1.0
 */
public class BibliotecaApp {
    private static Biblioteca biblioteca = new Biblioteca();
    private static Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        // Cargar datos de ejemplo
        cargarDatosEjemplo();
        
        boolean continuar = true;
        
        while (continuar) {
            mostrarMenu();
            int opcion = leerOpcion();
            
            switch (opcion) {
                case 1:
                    agregarLibro();
                    break;
                case 2:
                    listarLibros();
                    break;
                case 3:
                    buscarLibro();
                    break;
                case 4:
                    prestarLibro();
                    break;
                case 5:
                    devolverLibro();
                    break;
                case 6:
                    registrarUsuario();
                    break;
                case 7:
                    listarUsuarios();
                    break;
                case 8:
                    estadisticas();
                    break;
                case 9:
                    continuar = false;
                    System.out.println("\n¡Gracias por usar el Sistema de Biblioteca!");
                    System.out.println("¡Hasta pronto! 📚");
                    break;
                default:
                    System.out.println("\n❌ Opción inválida. Intente nuevamente.");
            }
            
            if (continuar) {
                pausar();
            }
        }
        
        scanner.close();
    }
    
    private static void mostrarMenu() {
        limpiarPantalla();
        System.out.println("╔════════════════════════════════════════════════╗");
        System.out.println("║     📚 SISTEMA DE GESTIÓN DE BIBLIOTECA 📚     ║");
        System.out.println("╠════════════════════════════════════════════════╣");
        System.out.println("║  1. ➕ Agregar nuevo libro                     ║");
        System.out.println("║  2. 📋 Listar todos los libros                 ║");
        System.out.println("║  3. 🔍 Buscar libro                            ║");
        System.out.println("║  4. 📤 Prestar libro                           ║");
        System.out.println("║  5. 📥 Devolver libro                          ║");
        System.out.println("║  6. 👤 Registrar nuevo usuario                 ║");
        System.out.println("║  7. 👥 Listar usuarios                         ║");
        System.out.println("║  8. 📊 Ver estadísticas                        ║");
        System.out.println("║  9. 🚪 Salir                                   ║");
        System.out.println("╚════════════════════════════════════════════════╝");
        System.out.print("\nSeleccione una opción: ");
    }
    
    private static int leerOpcion() {
        try {
            return Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            return -1;
        }
    }
    
    private static void agregarLibro() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("        ➕ AGREGAR NUEVO LIBRO");
        System.out.println("═══════════════════════════════════════");
        
        System.out.print("Título: ");
        String titulo = scanner.nextLine();
        
        System.out.print("Autor: ");
        String autor = scanner.nextLine();
        
        System.out.print("ISBN: ");
        String isbn = scanner.nextLine();
        
        System.out.print("Año de publicación: ");
        int anio = Integer.parseInt(scanner.nextLine());
        
        System.out.print("Categoría: ");
        String categoria = scanner.nextLine();
        
        Libro libro = new Libro(titulo, autor, isbn, anio, categoria);
        
        if (biblioteca.agregarLibro(libro)) {
            System.out.println("\n✅ ¡Libro agregado exitosamente!");
        } else {
            System.out.println("\n❌ Error: Ya existe un libro con ese ISBN.");
        }
    }
    
    private static void listarLibros() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("        📋 LISTADO DE LIBROS");
        System.out.println("═══════════════════════════════════════");
        
        if (biblioteca.getLibros().isEmpty()) {
            System.out.println("\n❌ No hay libros registrados en el sistema.");
            return;
        }
        
        System.out.println("\nTotal de libros: " + biblioteca.getLibros().size());
        System.out.println("─────────────────────────────────────────────────────────");
        
        for (Libro libro : biblioteca.getLibros()) {
            System.out.println(libro.toString());
            System.out.println("─────────────────────────────────────────────────────────");
        }
    }
    
    private static void buscarLibro() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("           🔍 BUSCAR LIBRO");
        System.out.println("═══════════════════════════════════════");
        
        System.out.println("\nBuscar por:");
        System.out.println("1. Título");
        System.out.println("2. Autor");
        System.out.println("3. ISBN");
        System.out.print("\nSeleccione opción: ");
        
        int opcion = leerOpcion();
        System.out.print("Ingrese término de búsqueda: ");
        String termino = scanner.nextLine();
        
        Libro[] resultados = null;
        
        switch (opcion) {
            case 1:
                resultados = biblioteca.buscarPorTitulo(termino);
                break;
            case 2:
                resultados = biblioteca.buscarPorAutor(termino);
                break;
            case 3:
                Libro libro = biblioteca.buscarPorISBN(termino);
                if (libro != null) {
                    resultados = new Libro[]{libro};
                }
                break;
            default:
                System.out.println("\n❌ Opción inválida.");
                return;
        }
        
        if (resultados != null && resultados.length > 0) {
            System.out.println("\n✅ Se encontraron " + resultados.length + " resultado(s):");
            System.out.println("─────────────────────────────────────────────────────────");
            for (Libro l : resultados) {
                System.out.println(l.toString());
                System.out.println("─────────────────────────────────────────────────────────");
            }
        } else {
            System.out.println("\n❌ No se encontraron resultados.");
        }
    }
    
    private static void prestarLibro() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("          📤 PRESTAR LIBRO");
        System.out.println("═══════════════════════════════════════");
        
        System.out.print("ISBN del libro: ");
        String isbn = scanner.nextLine();
        
        System.out.print("ID del usuario: ");
        String idUsuario = scanner.nextLine();
        
        if (biblioteca.prestarLibro(isbn, idUsuario)) {
            System.out.println("\n✅ ¡Préstamo realizado exitosamente!");
        } else {
            System.out.println("\n❌ Error: No se pudo realizar el préstamo.");
            System.out.println("Verifique que el libro esté disponible y el usuario exista.");
        }
    }
    
    private static void devolverLibro() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("          📥 DEVOLVER LIBRO");
        System.out.println("═══════════════════════════════════════");
        
        System.out.print("ISBN del libro: ");
        String isbn = scanner.nextLine();
        
        if (biblioteca.devolverLibro(isbn)) {
            System.out.println("\n✅ ¡Libro devuelto exitosamente!");
        } else {
            System.out.println("\n❌ Error: No se pudo devolver el libro.");
        }
    }
    
    private static void registrarUsuario() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("      👤 REGISTRAR NUEVO USUARIO");
        System.out.println("═══════════════════════════════════════");
        
        System.out.print("Nombre completo: ");
        String nombre = scanner.nextLine();
        
        System.out.print("Email: ");
        String email = scanner.nextLine();
        
        System.out.print("Teléfono: ");
        String telefono = scanner.nextLine();
        
        Usuario usuario = new Usuario(nombre, email, telefono);
        
        if (biblioteca.registrarUsuario(usuario)) {
            System.out.println("\n✅ ¡Usuario registrado exitosamente!");
            System.out.println("ID asignado: " + usuario.getId());
        } else {
            System.out.println("\n❌ Error: Ya existe un usuario con ese email.");
        }
    }
    
    private static void listarUsuarios() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("        👥 LISTADO DE USUARIOS");
        System.out.println("═══════════════════════════════════════");
        
        if (biblioteca.getUsuarios().isEmpty()) {
            System.out.println("\n❌ No hay usuarios registrados en el sistema.");
            return;
        }
        
        System.out.println("\nTotal de usuarios: " + biblioteca.getUsuarios().size());
        System.out.println("─────────────────────────────────────────────────────────");
        
        for (Usuario usuario : biblioteca.getUsuarios()) {
            System.out.println(usuario.toString());
            System.out.println("─────────────────────────────────────────────────────────");
        }
    }
    
    private static void estadisticas() {
        System.out.println("\n═══════════════════════════════════════");
        System.out.println("          📊 ESTADÍSTICAS");
        System.out.println("═══════════════════════════════════════");
        
        int totalLibros = biblioteca.getLibros().size();
        int librosPrestados = biblioteca.contarLibrosPrestados();
        int librosDisponibles = totalLibros - librosPrestados;
        int totalUsuarios = biblioteca.getUsuarios().size();
        
        System.out.println("\n📚 LIBROS:");
        System.out.println("   • Total: " + totalLibros);
        System.out.println("   • Disponibles: " + librosDisponibles);
        System.out.println("   • Prestados: " + librosPrestados);
        
        if (totalLibros > 0) {
            double porcentajePrestados = (librosPrestados * 100.0) / totalLibros;
            System.out.printf("   • Porcentaje prestado: %.2f%%\n", porcentajePrestados);
        }
        
        System.out.println("\n👥 USUARIOS:");
        System.out.println("   • Total registrados: " + totalUsuarios);
        System.out.println("   • Usuarios activos: " + biblioteca.contarUsuariosActivos());
        
        System.out.println("\n📈 CATEGORÍAS MÁS POPULARES:");
        String[] categorias = biblioteca.obtenerCategoriasPopulares();
        if (categorias.length > 0) {
            for (int i = 0; i < Math.min(3, categorias.length); i++) {
                System.out.println("   " + (i + 1) + ". " + categorias[i]);
            }
        } else {
            System.out.println("   Sin datos disponibles");
        }
    }
    
    private static void cargarDatosEjemplo() {
        // Agregar libros de ejemplo
        biblioteca.agregarLibro(new Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 1967, "Ficción"));
        biblioteca.agregarLibro(new Libro("El principito", "Antoine de Saint-Exupéry", "978-0156012195", 1943, "Infantil"));
        biblioteca.agregarLibro(new Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "978-8437604947", 1605, "Clásicos"));
        biblioteca.agregarLibro(new Libro("1984", "George Orwell", "978-0451524935", 1949, "Ficción"));
        biblioteca.agregarLibro(new Libro("Java: Cómo programar", "Paul Deitel", "978-6073237611", 2012, "Tecnología"));
        
        // Agregar usuarios de ejemplo
        biblioteca.registrarUsuario(new Usuario("María González", "maria.gonzalez@email.com", "555-0101"));
        biblioteca.registrarUsuario(new Usuario("Juan Pérez", "juan.perez@email.com", "555-0102"));
        biblioteca.registrarUsuario(new Usuario("Ana Martínez", "ana.martinez@email.com", "555-0103"));
    }
    
    private static void limpiarPantalla() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }
    
    private static void pausar() {
        System.out.print("\nPresione ENTER para continuar...");
        scanner.nextLine();
    }
}
