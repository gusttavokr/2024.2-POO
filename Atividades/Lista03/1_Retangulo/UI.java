import java.util.Scanner;

public class UI {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite a base e a altura do retângulo:");
        double base = leitor.nextDouble();
        double altura = leitor.nextDouble();
        Retangulo r1 = new Retangulo(base, altura);


        double area = r1.CalcArea();
        double diagonal = r1.CalcDiagonal();

        System.out.println(r1.ToString());
        System.out.println(String.format("A área do retângulo é %.2f", area));
        System.out.println(String.format("A diagonal do retângulo é %.2f", diagonal));

        leitor.close();

    }
}
