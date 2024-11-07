from cliente import Cliente, Clientes

class UI:
    def menu():
        print("1- Novo cliente, 2- Listar clientes, 9- fim")
        return int(input("Informe uma opção"))
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.inserir_cliente()
            if op == 2:
                UI.listar_cliente()
    @classmethod
    def inserir_cliente(cls):
        id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        cliente = Cliente(id, nome, email, fone)
    @classmethod
    def listar_cliente(cls):
        for cliente in Clientes.listar():
            print(cliente)

UI.main()