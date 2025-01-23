from Retangulo import Quadrado, Retangulo

while(True):
    print("\nEscolha uma das opções: \n")
    print("1- Retângulo, 2- Quadrado, 3- Sair")
    z = int(input())

    match z:
        case 1:
            x = int(input("Insira a base: "))
            y = int(input("Insira a altura: "))
            retangulo = Retangulo(x, y)
            print(retangulo)
        case 2:
            L = int(input("Insira o lado do Quadrado: "))
            quadrado = Quadrado(L)
            print(quadrado)
        case 3:
            break