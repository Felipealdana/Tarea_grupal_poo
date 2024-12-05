import java.util.*;
public class punto_10 {
    public static void main(String[] args) {
        Scanner entrada= new Scanner(System.in);
        int numeroinsc,Estracto;
        double Patrimonio,Pago;
        String Nombre;
        System.out.println("Ingrese el numero de inscripcion:");
        numeroinsc=entrada.nextInt();
        System.out.println("Ingrese el PRIMER nombre:");
        Nombre=entrada.next();
        System.out.println("Ingrese el patrimonio:");
        Patrimonio=entrada.nextDouble();
        System.out.println("Ingrese el estracto social:");
        Estracto=entrada.nextInt();
        if(Patrimonio>2000000 && Estracto>3 ) {
        Pago=50000+0.03*Patrimonio;
        }
        else {
        Pago=50000;
        }
        System.out.println("EL ESTUDIANTE CON NUMERO DE INSCRIPCION "+
        numeroinsc+" Y NOMBRE "+Nombre+" DEBE PAGAR "+Pago);
        }
}
