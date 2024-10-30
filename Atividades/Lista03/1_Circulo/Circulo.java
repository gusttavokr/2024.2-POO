public class Circulo {
    public float raio = 5.0f;
    public float area;
    public float circunf;
    private float pi = 3.14f;

    public float getraio(){
        return this.raio;
    }
    public void setraio(int r){
        this.raio = r;
    }

    public float getpi(){
        return this.pi;
    }
    public void setpi(float p){
        this.pi = p;
    }

    public void area(){
        area = getpi()*(getraio()*getraio());
        System.out.println("A área desse círculo é: " + area);
    }
    public void circunf(){
        circunf = (2*getpi())*getraio();
        System.out.println("A circunferência desse círculo é: " + circunf);
    }
}
