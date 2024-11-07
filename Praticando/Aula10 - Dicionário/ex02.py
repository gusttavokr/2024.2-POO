import json

class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    
    def __str__(self):
        return f"{self.id} - {self.nome}"
    

def salvar():
    a = Cliente(1, "Gusta")
    b = Cliente(2, "Maiquinho")

    print(a)
    print(b)
    print(a.__dict__)
    print(b.__dict__)
    # Dict ou vars transformam a variável em dicionário
    print(vars(a))
    print(vars(b))

    clientes = [a,b]

    with open ("clientes.json", mode="w") as arquivo:
        # abra um arquivo (nome do arquivo), no modo de leitura para (variável)
        json.dump(clientes, arquivo, default = vars)
        # passe clientes para a variável em dicionário
def abrir():
    clientes = []
    with open ("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
            c = Cliente(obj["id"], obj["nome"])
            clientes.append(c)
    for c in clientes:
        print(c)

abrir()