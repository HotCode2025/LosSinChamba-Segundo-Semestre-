package clase11;


public class ProductoImparesScanner {
        public static void main(String[] args) {
        
        long producto = 1; 
        int contador = 0;
       
            for (int i = 1; i < 20; i+=2) {
                producto *= i;
            }
            System.out.println("Cantidad de impares: " + contador);
        
        /*
            for (int i = 1; contador < 10; i++) {
                if (i % 2 != 0) {
                    producto *= i;
                    contador++;
                }

            }
        */
        System.out.println("El producto de los 10 primeros números impares es: " + producto);
    }
}
