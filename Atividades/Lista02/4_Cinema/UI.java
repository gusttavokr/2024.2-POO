import java.util.Scanner;

public class UI {
    public static void main(String[] args) {
        Cinema c1 = new Cinema();
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o dia do filme:");
        c1.setdia(leitor.nextLine());
        System.out.println("Digite o horário do filme:");
        c1.sethorario(leitor.nextDouble());

        double valor = c1.Ingresso();
        System.out.println(String.format("Seu ingresso custará: R$ %.2f", valor));

        leitor.close();
    }
}