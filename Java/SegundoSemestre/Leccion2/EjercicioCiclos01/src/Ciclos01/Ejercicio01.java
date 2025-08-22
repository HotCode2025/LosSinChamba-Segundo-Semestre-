/*
Ejercicio 1: Leer un número y mostrar su cuadrado, repetir
el proceso hasta que se introduzca un número negativo
*/
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio01 {
    public static void main(String[] args) {
        int numero, cuadrado;
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Dijite un número: "));
        while(numero >= 0){ //Minetras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero "+numero+" elevado al cuadrado es: "+cuadrado);
            System.out.println("Dijite otro numero: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Dijite otro número: "));   
        }
        System.out.println("El programa a finalizado por numero negativo");
    }  
}
