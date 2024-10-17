#include <stdio.h>

int main(){
    int base;
    int altura;

    printf("Digite a base e a altura do triângulo: ");
    scanf("%d %d", &base, &altura);

    int calculo = (base*altura)/2;
    printf("A área do triângulo é: %d\n", calculo);
    return 0;
}