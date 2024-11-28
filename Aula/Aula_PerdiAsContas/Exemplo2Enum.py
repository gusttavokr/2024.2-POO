import enum

class Dia(enum.IntFlag):
    Domingo = 1
    Segunda = 2
    Terça = 4
    Quarta = 8
    Quinta = 16
    Sexta = 32
    Sábado = 64

a = Dia.Quarta
print(a, type(a))
print(a.name, type(a.name))
print(a.value, type(a.value))