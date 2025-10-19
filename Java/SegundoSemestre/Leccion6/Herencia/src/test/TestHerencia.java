package test;

import domain.Empleado;
import domain.Cliente;
import java.util.Date;
        
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ariel", 65000.00);
        System.out.println("empleado1 = " + empleado1);
        Date fecha1 = new Date();
        Cliente cl1 = new Cliente(fecha1, true, "Gabriel", 'M', 40, "Independencia 41");
        System.out.println("Cliente: " + cl1);
    }
}