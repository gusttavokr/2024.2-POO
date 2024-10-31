import java.util.Scanner;

public class UI {
    public static void main(String[] args) {
        Cinema c1 = new Cinema();
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite o dia do filme:");
        c1.setdia(leitor.nextLine());

        leitor.close();
    }
}