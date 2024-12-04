import java.util.*;

public class punto_7 {
    public static void main(String[] args) {
        double M,R;
        Scanner entrada= new Scanner(System.in);
        System.out.println("Ingrese el primer numero");
        M=entrada.nextInt();
        System.out.println("Ingrese el segundo numero");
        R=entrada.nextInt();
        if(M>R) {
        System.out.println("el primer numero es mayor");
        }
        else if(M<R) {
        System.out.println("el segundo numero es mayor");
        }
        else {
        System.out.println("los numeros son iguales");
        }
        }
}
