from Frete import Frete, FreteExpresso

print("BEM-VINDO AO SEU SITE DE FRETE")

while(True):
    print("Escolha o tipo de frete: ")
    print("1- Frete normal, 2- Frete Expresso, 3- Sair")

    z = int(input("Digite aqui: "))

    match z:
        case 1:
            x = float(input("Informe a distância: "))
            y = float(input("Informe o peso: "))
            frete = Frete(x, y)
            print(frete)
        case 2:
            x = float(input("Informe a distância: "))
            y = float(input("Informe o peso: "))
            z = float(input("Informe o valor do seguro: "))
            freteExp = FreteExpresso(x)
            print(freteExp)
        case 3:
            break