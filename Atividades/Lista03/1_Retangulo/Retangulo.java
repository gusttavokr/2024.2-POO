public class Retangulo {
    private double base;
    private double altura;

    public Retangulo(double b, double a){
        this.base = b;
        this.altura = a;
    }

    public String ToString(){
        return "Retangulo { Base: "+ base + ", Altura: " + altura + "}";
    }

    public double getbase(){
        return this.base;
    }
    public double getaltura(){
        return this.altura;
    }
    public void setbase(double b){
        this.base = b;
    }
    public void setaltura(double a){
        this.altura = a;
    }

    public double CalcArea(){
        double area = getbase() * getaltura();
        return area;
    }
    public double CalcDiagonal(){
        double diagonal = Math.sqrt((getbase()*getbase())+(getaltura()*getaltura()));
        return diagonal;
    }
}
