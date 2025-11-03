package com.biblioteca.controlador;

import com.biblioteca.modelo.Libro;
import com.biblioteca.modelo.Usuario;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Clase Biblioteca - Gestiona la colección de libros y usuarios
 * Implementa la lógica de negocio con:
 * - Bucles (for, while, foreach)
 * - Condicionales (if-else, switch)
 * - Manejo de colecciones
 * 
 * @author Los Sin Chamba
 * @version 1.0
 */
public class Biblioteca {
    // Atributos
    private List<Libro> libros;
    private List<Usuario> usuarios;
    private final int LIMITE_PRESTAMOS_USUARIO = 3;
    
    // Constructor
    public Biblioteca() {
        this.libros = new ArrayList<>();
        this.usuarios = new ArrayList<>();
    }
    
    // Getters
    public List<Libro> getLibros() {
        return new ArrayList<>(libros);
    }
    
    public List<Usuario> getUsuarios() {
        return new ArrayList<>(usuarios);
    }
    
    // ===== MÉTODOS DE GESTIÓN DE LIBROS =====
    
    /**
     * Agrega un nuevo libro a la biblioteca
     * Usa condicionales para validación
     * @param libro Libro a agregar
     * @return true si se agregó exitosamente
     */
    public boolean agregarLibro(Libro libro) {
        // Condicional: Verificar si el libro ya existe
        if (libro == null) {
            return false;
        }
        
        // Bucle: Verificar duplicados por ISBN
        for (Libro l : libros) {
            if (l.getIsbn().equals(libro.getIsbn())) {
                return false; // Ya existe
            }
        }
        
        return libros.add(libro);
    }
    
    /**
     * Busca un libro por ISBN
     * Usa bucle y condicional
     * @param isbn ISBN del libro
     * @return Libro encontrado o null
     */
    public Libro buscarPorISBN(String isbn) {
        // Bucle for mejorado con condicional
        for (Libro libro : libros) {
            if (libro.getIsbn().equals(isbn)) {
                return libro;
            }
        }
        return null;
    }
    
    /**
     * Busca libros por título (búsqueda parcial)
     * Usa bucles y condicionales anidados
     * @param titulo Título o parte del título
     * @return Array de libros encontrados
     */
    public Libro[] buscarPorTitulo(String titulo) {
        List<Libro> resultados = new ArrayList<>();
        
        // Bucle con condicional para búsqueda parcial
        for (int i = 0; i < libros.size(); i++) {
            Libro libro = libros.get(i);
            if (libro.getTitulo().toLowerCase().contains(titulo.toLowerCase())) {
                resultados.add(libro);
            }
        }
        
        // Convertir lista a array
        return resultados.toArray(new Libro[0]);
    }
    
    /**
     * Busca libros por autor
     * Usa bucle while y condicional
     * @param autor Nombre del autor
     * @return Array de libros del autor
     */
    public Libro[] buscarPorAutor(String autor) {
        List<Libro> resultados = new ArrayList<>();
        int indice = 0;
        
        // Bucle while con condicional
        while (indice < libros.size()) {
            Libro libro = libros.get(indice);
            if (libro.getAutor().toLowerCase().contains(autor.toLowerCase())) {
                resultados.add(libro);
            }
            indice++;
        }
        
        return resultados.toArray(new Libro[0]);
    }
    
    /**
     * Cuenta los libros prestados
     * Usa bucle y condicional
     * @return Número de libros prestados
     */
    public int contarLibrosPrestados() {
        int contador = 0;
        
        // Bucle for con condicional
        for (Libro libro : libros) {
            if (!libro.isDisponible()) {
                contador++;
            }
        }
        
        return contador;
    }
    
    /**
     * Obtiene las categorías más populares
     * Usa bucles, condicionales y Map
     * @return Array de categorías ordenadas por popularidad
     */
    public String[] obtenerCategoriasPopulares() {
        Map<String, Integer> conteoCategoria = new HashMap<>();
        
        // Bucle: Contar libros por categoría
        for (Libro libro : libros) {
            String categoria = libro.getCategoria();
            
            // Condicional: Incrementar contador
            if (conteoCategoria.containsKey(categoria)) {
                conteoCategoria.put(categoria, conteoCategoria.get(categoria) + 1);
            } else {
                conteoCategoria.put(categoria, 1);
            }
        }
        
        // Ordenar categorías por popularidad (bubble sort con bucles anidados)
        List<String> categorias = new ArrayList<>(conteoCategoria.keySet());
        
        // Bucles anidados para ordenamiento
        for (int i = 0; i < categorias.size() - 1; i++) {
            for (int j = 0; j < categorias.size() - i - 1; j++) {
                String cat1 = categorias.get(j);
                String cat2 = categorias.get(j + 1);
                
                // Condicional: Comparar y ordenar
                if (conteoCategoria.get(cat1) < conteoCategoria.get(cat2)) {
                    categorias.set(j, cat2);
                    categorias.set(j + 1, cat1);
                }
            }
        }
        
        return categorias.toArray(new String[0]);
    }
    
    // ===== MÉTODOS DE GESTIÓN DE USUARIOS =====
    
    /**
     * Registra un nuevo usuario
     * Usa condicionales para validación
     * @param usuario Usuario a registrar
     * @return true si se registró exitosamente
     */
    public boolean registrarUsuario(Usuario usuario) {
        // Condicional: Validar datos
        if (usuario == null || usuario.getEmail() == null || usuario.getEmail().isEmpty()) {
            return false;
        }
        
        // Bucle: Verificar duplicados por email
        for (Usuario u : usuarios) {
            if (u.getEmail().equals(usuario.getEmail())) {
                return false;
            }
        }
        
        return usuarios.add(usuario);
    }
    
    /**
     * Busca un usuario por ID
     * Usa bucle y condicional
     * @param id ID del usuario
     * @return Usuario encontrado o null
     */
    public Usuario buscarUsuarioPorId(String id) {
        // Bucle con condicional
        for (Usuario usuario : usuarios) {
            if (usuario.getId().equals(id)) {
                return usuario;
            }
        }
        return null;
    }
    
    /**
     * Cuenta los usuarios activos (con préstamos)
     * Usa bucle y condicional
     * @return Número de usuarios activos
     */
    public int contarUsuariosActivos() {
        int contador = 0;
        
        // Bucle for con condicional
        for (int i = 0; i < usuarios.size(); i++) {
            if (usuarios.get(i).esActivo()) {
                contador++;
            }
        }
        
        return contador;
    }
    
    // ===== MÉTODOS DE PRÉSTAMO Y DEVOLUCIÓN =====
    
    /**
     * Presta un libro a un usuario
     * Usa múltiples condicionales y validaciones
     * @param isbn ISBN del libro
     * @param idUsuario ID del usuario
     * @return true si el préstamo fue exitoso
     */
    public boolean prestarLibro(String isbn, String idUsuario) {
        // Buscar el libro
        Libro libro = buscarPorISBN(isbn);
        
        // Condicional: Verificar que el libro existe
        if (libro == null) {
            System.out.println("Error: Libro no encontrado.");
            return false;
        }
        
        // Condicional: Verificar disponibilidad
        if (!libro.isDisponible()) {
            System.out.println("Error: El libro no está disponible.");
            return false;
        }
        
        // Buscar el usuario
        Usuario usuario = buscarUsuarioPorId(idUsuario);
        
        // Condicional: Verificar que el usuario existe
        if (usuario == null) {
            System.out.println("Error: Usuario no encontrado.");
            return false;
        }
        
        // Condicional: Verificar límite de préstamos
        if (!usuario.puedePrestar(LIMITE_PRESTAMOS_USUARIO)) {
            System.out.println("Error: El usuario alcanzó el límite de " + 
                             LIMITE_PRESTAMOS_USUARIO + " libros.");
            return false;
        }
        
        // Realizar el préstamo
        boolean prestamoExitoso = libro.prestar(idUsuario);
        
        // Condicional: Verificar si el préstamo fue exitoso
        if (prestamoExitoso) {
            usuario.registrarPrestamo(isbn);
            return true;
        }
        
        return false;
    }
    
    /**
     * Devuelve un libro a la biblioteca
     * Usa condicionales y bucles
     * @param isbn ISBN del libro
     * @return true si la devolución fue exitosa
     */
    public boolean devolverLibro(String isbn) {
        // Buscar el libro
        Libro libro = buscarPorISBN(isbn);
        
        // Condicional: Verificar que el libro existe
        if (libro == null) {
            return false;
        }
        
        // Condicional: Verificar que el libro estaba prestado
        if (libro.isDisponible()) {
            System.out.println("Error: El libro ya está disponible.");
            return false;
        }
        
        // Obtener el usuario que tiene el libro
        String idUsuario = libro.getUsuarioPrestamo();
        
        // Realizar la devolución
        boolean devolucionExitosa = libro.devolver();
        
        // Condicional: Actualizar el usuario
        if (devolucionExitosa && idUsuario != null) {
            Usuario usuario = buscarUsuarioPorId(idUsuario);
            
            // Condicional anidado: Verificar que se encontró al usuario
            if (usuario != null) {
                usuario.registrarDevolucion();
            }
            
            return true;
        }
        
        return false;
    }
    
    /**
     * Genera un reporte de libros disponibles vs prestados
     * Usa bucles, condicionales y switch
     * @return String con el reporte
     */
    public String generarReporte() {
        StringBuilder reporte = new StringBuilder();
        reporte.append("===== REPORTE DE BIBLIOTECA =====\n\n");
        
        int disponibles = 0;
        int prestados = 0;
        Map<String, Integer> porCategoria = new HashMap<>();
        
        // Bucle: Analizar cada libro
        for (Libro libro : libros) {
            // Condicional: Clasificar por estado
            if (libro.isDisponible()) {
                disponibles++;
            } else {
                prestados++;
            }
            
            // Contar por categoría
            String categoria = libro.getCategoria();
            porCategoria.put(categoria, porCategoria.getOrDefault(categoria, 0) + 1);
        }
        
        reporte.append("Total de libros: ").append(libros.size()).append("\n");
        reporte.append("Disponibles: ").append(disponibles).append("\n");
        reporte.append("Prestados: ").append(prestados).append("\n\n");
        
        reporte.append("Por categoría:\n");
        
        // Bucle: Mostrar categorías
        for (Map.Entry<String, Integer> entry : porCategoria.entrySet()) {
            reporte.append("  - ").append(entry.getKey())
                   .append(": ").append(entry.getValue()).append("\n");
        }
        
        return reporte.toString();
    }
}
