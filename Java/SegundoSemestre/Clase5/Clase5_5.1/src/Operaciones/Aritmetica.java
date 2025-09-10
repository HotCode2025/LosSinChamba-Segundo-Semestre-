package Operaciones;

public class Aritmetica {
    int a,b;
    public void sumarNumeros() {
        int resultado = a + b;
        System.out.println("Resultado= " + resultado);
    }
    public int sumarConRetorno() {
        return a + b;
    }
}
