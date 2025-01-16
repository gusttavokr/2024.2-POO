class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __str__(self):
        return f"{self.nome}, {self.idade}"
    
    # Método de comparação para ordenar os alunos
    def __lt__(self, other):
        return self.nome < other.nome
    
x = []
x.append(Aluno("Ícaro", 19))
x.append(Aluno("Emanuelly", 20))
x.append(Aluno("Gustavo", 18))

x.sort()

for p in x:
    print(p)