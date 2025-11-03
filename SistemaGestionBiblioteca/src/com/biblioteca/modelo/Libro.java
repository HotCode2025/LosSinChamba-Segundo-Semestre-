package com.biblioteca.modelo;

/**
 * Clase Libro - Representa un libro en la biblioteca
 * Implementa Programación Orientada a Objetos con:
 * - Encapsulamiento (atributos privados)
 * - Getters y Setters
 * - Constructor
 * - Métodos de negocio
 * 
 * @author Los Sin Chamba
 * @version 1.0
 */
public class Libro {
    // Atributos privados (Encapsulamiento)
    private String titulo;
    private String autor;
    private String isbn;
    private int anioPublicacion;
    private String categoria;
    private boolean disponible;
    private String usuarioPrestamo;
    
    // Constructor
    public Libro(String titulo, String autor, String isbn, int anioPublicacion, String categoria) {
        this.titulo = titulo;
        this.autor = autor;
        this.isbn = isbn;
        this.anioPublicacion = anioPublicacion;
        this.categoria = categoria;
        this.disponible = true;
        this.usuarioPrestamo = null;
    }
    
    // Getters y Setters
    public String getTitulo() {
        return titulo;
    }
    
    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }
    
    public String getAutor() {
        return autor;
    }
    
    public void setAutor(String autor) {
        this.autor = autor;
    }
    
    public String getIsbn() {
        return isbn;
    }
    
    public void setIsbn(String isbn) {
        this.isbn = isbn;
    }
    
    public int getAnioPublicacion() {
        return anioPublicacion;
    }
    
    public void setAnioPublicacion(int anioPublicacion) {
        this.anioPublicacion = anioPublicacion;
    }
    
    public String getCategoria() {
        return categoria;
    }
    
    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }
    
    public boolean isDisponible() {
        return disponible;
    }
    
    public void setDisponible(boolean disponible) {
        this.disponible = disponible;
    }
    
    public String getUsuarioPrestamo() {
        return usuarioPrestamo;
    }
    
    public void setUsuarioPrestamo(String usuarioPrestamo) {
        this.usuarioPrestamo = usuarioPrestamo;
    }
    
    // Métodos de negocio
    
    /**
     * Presta el libro a un usuario
     * @param idUsuario ID del usuario que toma prestado el libro
     * @return true si se prestó exitosamente, false si no estaba disponible
     */
    public boolean prestar(String idUsuario) {
        if (this.disponible) {
            this.disponible = false;
            this.usuarioPrestamo = idUsuario;
            return true;
        }
        return false;
    }
    
    /**
     * Devuelve el libro a la biblioteca
     * @return true si se devolvió exitosamente
     */
    public boolean devolver() {
        if (!this.disponible) {
            this.disponible = true;
            this.usuarioPrestamo = null;
            return true;
        }
        return false;
    }
    
    /**
     * Verifica si el libro fue publicado antes de un año específico
     * @param anio Año de referencia
     * @return true si fue publicado antes del año especificado
     */
    public boolean esAntiguo(int anio) {
        return this.anioPublicacion < anio;
    }
    
    /**
     * Obtiene la edad del libro en años
     * @param anioActual Año actual para el cálculo
     * @return Edad del libro en años
     */
    public int getEdad(int anioActual) {
        return anioActual - this.anioPublicacion;
    }
    
    /**
     * Verifica si el título o autor contienen un término de búsqueda
     * @param termino Término a buscar
     * @return true si se encuentra el término
     */
    public boolean coincideBusqueda(String termino) {
        String terminoLower = termino.toLowerCase();
        return this.titulo.toLowerCase().contains(terminoLower) ||
               this.autor.toLowerCase().contains(terminoLower);
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("📖 ").append(titulo).append("\n");
        sb.append("   Autor: ").append(autor).append("\n");
        sb.append("   ISBN: ").append(isbn).append("\n");
        sb.append("   Año: ").append(anioPublicacion).append("\n");
        sb.append("   Categoría: ").append(categoria).append("\n");
        sb.append("   Estado: ");
        
        if (disponible) {
            sb.append("✅ Disponible");
        } else {
            sb.append("❌ Prestado (Usuario: ").append(usuarioPrestamo).append(")");
        }
        
        return sb.toString();
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        Libro libro = (Libro) obj;
        return isbn.equals(libro.isbn);
    }
    
    @Override
    public int hashCode() {
        return isbn.hashCode();
    }
}
