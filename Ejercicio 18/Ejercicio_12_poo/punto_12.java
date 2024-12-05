import java.util.Scanner;
public class punto_12 {
    public static void main(String[] args) {
        double Valorh, Salario;
        String Nombre;
         int Horatrab ;
        Scanner entrada= new Scanner(System.in);
        System.out.println("Nombre del trabajador");
        Nombre = entrada.next();
        System.out.println("Numero de horas trabajadas");
        Horatrab = entrada.nextInt();
        System.out.println("Valor hora de trabajo");
        Valorh = entrada.nextDouble();
        if (Horatrab > 40) {
        Horatrab = Horatrab - 40;
        if (Horatrab > 8) {
        Horatrab = Horatrab - 8;
        Salario = (40*Valorh) + (Valorh*2*8) + (Valorh*3*Horatrab);
        }
        else {
        Salario = (Valorh * 40) + (Horatrab*2*Valorh);
        }
        }
        else {
        Salario = (Horatrab * Valorh);
        }
        System.out.println("El trabajador " + Nombre);
        System.out.println("Recibe un salario de $" + Salario);
        }
}
