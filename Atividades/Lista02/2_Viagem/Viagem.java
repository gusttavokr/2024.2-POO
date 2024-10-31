public class Viagem {
    private double distancia, tempo;

    public double getdistancia(){
        return this.distancia;
    }
    public double gettempo(){
        return this.tempo;
    }
    public void setdistancia(double d){
        this.distancia = d;
    }
    public void settempo(double t){
        this.tempo = t;
    }

    public double velocidadeMedia(){
        double velocidade = (getdistancia()/gettempo());
        System.out.println(String.format("A velocidade média da viagem é: %.2f km/h", velocidade));
        return velocidade;
    }
}