import json
from Cliente import Cliente, Clientes

class UI:
    def menu():
        print("1- Novo cliente, 2- Listar Clientes\n9- Fim")
        return int(input("Digite uma opção: "))
    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.inserir_cliente()
            if op == 2:
                UI.listar_clientes()

    @classmethod
    def inserir_cliente(cls):
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o fone: ")
        cliente = Cliente(0, nome, email, fone)
        Clientes.inserir(cliente)

    @classmethod
    def listar_clientes(cls):
        clientes = Clientes.listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in clientes:
                print(cliente)

UI.main()