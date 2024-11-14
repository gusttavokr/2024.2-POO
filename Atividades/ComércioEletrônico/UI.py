import json
from Cliente import Cliente, Clientes

class UI:
    def menu():
        print("1- Novo cliente, 2- Listar Clientes, 9- Fim")
        return int(input("Digite uma opção: "))
    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.inserir_cliente()

    @classmethod
    def inserir_cliente(cls):
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        fone = input("Digite o fone: ")
        cliente = Cliente(0, nome, email, fone)
        Clientes.inserir(cliente)
UI.main()