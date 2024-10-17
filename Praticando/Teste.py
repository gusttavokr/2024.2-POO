class triangulo:
  def __init__(self):
    self.b = 0
    self.h = 0
  def calc_area(self):
    return (self.b*self.h)/2

x = triangulo()

x.b = float(input("Informe o valor da base:"))
x.h = float(input("Informe o valor da altura:"))
print(f"Área = {x.calc_area()}")
