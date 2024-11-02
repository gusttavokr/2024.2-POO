package Praticando;
class Pessoa {
    private String nome;
    private int idade;

    public Pessoa(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    // Sobrescrevendo o método toString para exibir informações sobre a pessoa
    @Override
    public String toString() {
        return "Pessoa { Nome: " + nome + ", Idade: " + idade + " }";
    }
}

public class Main {
    public static void main(String[] args) {
        Pessoa pessoa = new Pessoa("Ana", 25);

        // Exibindo o objeto no terminal
        System.out.println(pessoa); // Chamará automaticamente o método toString()
    }
}