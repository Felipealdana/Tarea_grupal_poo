import java.util.*;
public class punto_11 {
    public static void main(String[] args) {
        double A,B,C;
       Scanner entrada= new Scanner(System.in);
       System.out.println("ingresa 3 numeros distintos");
       System.out.println("ingresa el primer numero: ");
       A=entrada.nextDouble();
       System.out.println("ingresa el segundo numero: ");
       B=entrada.nextDouble();
       System.out.println("ingresa el tercero numero: ");
       C=entrada.nextDouble();
       if(A>B && A>C){
       System.out.println("el primer numero es mayor: "+A);
       }
       else if(B>A &&B>C) {
       System.out.println("el segundo numero es mayor: "+B);
       }
       else {
       System.out.println("el tercer numero es mayor: "+C);
       }
       }
}
