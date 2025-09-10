package Operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica = new Aritmetica();
        aritmetica.a = 4;
        aritmetica.b = 2; 
        aritmetica.sumarNumeros();
        
        int resultado = aritmetica.sumarConRetorno();
        System.out.println("Resultado = " + resultado);
        
        
        // Clase 5.3
        resultado = aritmetica.sumarConArgumentos(8, 9);
        System.out.println("Resultado usando argumentos = " + resultado);
    }
}
