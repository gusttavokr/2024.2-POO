import java.util.Scanner;

public class UI {
    public static void main(String[] args) {
        Banco c1 = new Banco();
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite o nome do titular:");
        c1.settitular(leitor.nextLine());
        System.out.println("Digite o número da conta");
        c1.setnumConta(leitor.nextInt());

        System.out.println("Deposite um valor:");
        c1.depositar(leitor.nextDouble());
        System.out.println("Saque um valor:");
        c1.sacar(leitor.nextDouble());
        leitor.close();
    }
}
