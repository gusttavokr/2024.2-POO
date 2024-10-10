print("Digite a base e a altura do retângulo:")
base = int(input())
altura = int(input())

area = base*altura
perimetro = base*2+altura*2
diagonal = (base**2+altura**2)**0.5

area = "{:.2f}".format(area)
perimetro = "{:.2f}".format(perimetro)
diagonal = "{:.2f}".format(diagonal)

print(f"Área = {area} - Perímetro = {perimetro} - Diagonal = {diagonal}")