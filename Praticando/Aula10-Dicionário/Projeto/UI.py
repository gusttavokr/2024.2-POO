from cliente import Cliente, Clientes

class UI:
    def menu():
        print("1- Novo cliente, 2- Listar clientes, 3- Atualizar clientes, 9- fim")
        return int(input("Informe uma opção: "))
    
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1:
                UI.inserir_cliente()
            if op == 2:
                UI.listar_cliente()
            if op == 3:
                UI.atualizar_clientes()

    @classmethod
    def inserir_cliente(cls):
        # id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        email = input("Informe o email: ")
        fone = input("Informe o fone: ")
        cliente = Cliente(0, nome, email, fone)
        Clientes.inserir(cliente)

    @classmethod
    def listar_cliente(cls):
        clientes = Clientes.listar()
        if len(clientes) == 0:
            print("Nenhum cliente cadastrado")
        else:
            for cliente in Clientes.listar():
                print(cliente)
                
    @classmethod
    def atualizar_clientes(cls):
        cls.listar_cliente()
        id = int(input("Informe o id do cliente a ser akterado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo email: ")
        fone = input("Informe o novo fone: ")
        cliente = Cliente(id, nome, email, fone)
        Clientes.atualizar(cliente)
UI.main()