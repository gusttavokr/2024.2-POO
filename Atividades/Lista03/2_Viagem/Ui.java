import java.util.Scanner;

public class Ui{
    public static void main(String[] args) {
        Viagem v1 = new Viagem();
        Scanner leitor = new Scanner(System.in);

        System.out.println("Informe a distância da viagem:");
        v1.setdistancia(leitor.nextDouble());
        System.out.println("Informe o tempo da viagem:");
        v1.settempo(leitor.nextDouble());
        v1.velocidadeMedia();

        leitor.close();
    }
}