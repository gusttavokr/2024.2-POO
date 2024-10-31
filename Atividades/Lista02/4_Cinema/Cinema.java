public class Cinema {
    private String dia;
    private double horario;
    public double ingresso = 0.00;

    public String getdia(){
        return this.dia;
    }
    public double gethorário(){
        return this.horario;
    }
    public double getingresso(){
        return this.ingresso;
    }
    public void setdia(String d){
        this.dia = d;
    }
    public void sethorário(double h){
        this.horario = h;
    } 
    public void setingresso(double i){
        this.ingresso = i;
    }

    public double Ingresso(){
        if (getdia().equals("Segunda")|| getdia().equals("Terça") || getdia().equals("Quinta")){
            setingresso(16.00);
        }
        else if (getdia().equals("Quarta")) {
            setingresso(8.00);
        }
        else if (getdia().equals("Sexta") || getdia().equals("Sábado") || getdia().equals("Domingo")) {
            setingresso(20.00);
        }
        if (gethorário()>=17 && gethorário() <= 24) {
            setingresso(getingresso()*0.5);
        }
        return getingresso();
    }
}
