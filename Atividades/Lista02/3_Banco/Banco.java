public class Banco {
    private String titular;
    private int numConta;
    private double saldo = 0.00;

    public String gettitular(){
        return this.titular;
    }
    public int getnumConta(){
        return this.numConta;
    }
    public double getsaldo(){
        return this.saldo;
    }

    public void settitular(String t){
        this.titular = t;
    }
    public void setnumConta(int c){
        this.numConta = c;
    }
    public void setsaldo(double s){
        this.saldo = s;
    }

    public double depositar(double deposito){
        setsaldo(deposito + getsaldo());
        System.out.println(String.format("Você depositou %.2f, seu saldo agora é: %.2f", deposito, getsaldo()));
        return getsaldo();
    }

    public double sacar(double saque){
        if (saque > getsaldo()) {
            System.out.println("Você não pode sacar esse valor seu porra!");
            saque = 0;
            sacar(saque);
        }
        else {
            setsaldo(getsaldo()- saque);
            System.out.println(String.format("Você sacou %.2f, seu saldo agora é: %.2f", saque, getsaldo()));
        }
        return getsaldo();
    }
}
