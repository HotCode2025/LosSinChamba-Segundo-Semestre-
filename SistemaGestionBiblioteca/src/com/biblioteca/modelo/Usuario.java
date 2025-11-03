package com.biblioteca.modelo;

import java.util.ArrayList;
import java.util.List;

/**
 * Clase Usuario - Representa un usuario de la biblioteca
 * Implementa POO con encapsulamiento y métodos de negocio
 * 
 * @author Los Sin Chamba
 * @version 1.0
 */
public class Usuario {
    // Atributos privados
    private String id;
    private String nombre;
    private String email;
    private String telefono;
    private List<String> historialPrestamos;
    private int librosPrestadosActualmente;
    private static int contadorUsuarios = 1000;
    
    // Constructor
    public Usuario(String nombre, String email, String telefono) {
        this.id = "USR" + (contadorUsuarios++);
        this.nombre = nombre;
        this.email = email;
        this.telefono = telefono;
        this.historialPrestamos = new ArrayList<>();
        this.librosPrestadosActualmente = 0;
    }
    
    // Getters y Setters
    public String getId() {
        return id;
    }
    
    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    
    public String getEmail() {
        return email;
    }
    
    public void setEmail(String email) {
        this.email = email;
    }
    
    public String getTelefono() {
        return telefono;
    }
    
    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }
    
    public List<String> getHistorialPrestamos() {
        return new ArrayList<>(historialPrestamos);
    }
    
    public int getLibrosPrestadosActualmente() {
        return librosPrestadosActualmente;
    }
    
    // Métodos de negocio
    
    /**
     * Verifica si el usuario puede tomar más libros prestados
     * @param limite Límite máximo de libros simultáneos
     * @return true si puede tomar más libros
     */
    public boolean puedePrestar(int limite) {
        return librosPrestadosActualmente < limite;
    }
    
    /**
     * Registra un nuevo préstamo para el usuario
     * @param isbn ISBN del libro prestado
     */
    public void registrarPrestamo(String isbn) {
        historialPrestamos.add(isbn);
        librosPrestadosActualmente++;
    }
    
    /**
     * Registra la devolución de un libro
     */
    public void registrarDevolucion() {
        if (librosPrestadosActualmente > 0) {
            librosPrestadosActualmente--;
        }
    }
    
    /**
     * Verifica si el usuario es activo (tiene libros prestados)
     * @return true si tiene libros prestados actualmente
     */
    public boolean esActivo() {
        return librosPrestadosActualmente > 0;
    }
    
    /**
     * Obtiene el total de préstamos históricos
     * @return Número total de libros que ha tomado prestados
     */
    public int getTotalPrestamos() {
        return historialPrestamos.size();
    }
    
    /**
     * Verifica si el usuario ha prestado un libro específico antes
     * @param isbn ISBN del libro a verificar
     * @return true si el libro está en el historial
     */
    public boolean haPrestado(String isbn) {
        return historialPrestamos.contains(isbn);
    }
    
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("👤 ").append(nombre).append(" (").append(id).append(")\n");
        sb.append("   Email: ").append(email).append("\n");
        sb.append("   Teléfono: ").append(telefono).append("\n");
        sb.append("   Libros actuales: ").append(librosPrestadosActualmente).append("\n");
        sb.append("   Total préstamos: ").append(historialPrestamos.size()).append("\n");
        sb.append("   Estado: ");
        
        if (esActivo()) {
            sb.append("🟢 Activo");
        } else {
            sb.append("⚪ Inactivo");
        }
        
        return sb.toString();
    }
    
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        
        Usuario usuario = (Usuario) obj;
        return email.equals(usuario.email);
    }
    
    @Override
    public int hashCode() {
        return email.hashCode();
    }
}
