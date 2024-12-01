from Models.Cliente import Cliente, Clientes
from Models.Categoria import Categoria, Categorias
from Models.Produto import Produto, Produtos

class View:

    @staticmethod
    def inserir_cliente(nome, email, fone):
        cliente = Cliente(1, nome, email, fone) 
        Clientes.inserir(cliente)

    @staticmethod
    def listar_clientes():
        return Clientes.listar()
    
    @staticmethod
    def atualizar_clientes(id, nome, email, fone):
        cliente = Cliente(id, nome, email, fone)
        Clientes.atualizar(cliente) # Usando o método atualizar na variável cliente

    @staticmethod
    def excluir_clientes(id):
        Clientes.excluir(Clientes.listar_id(id))

    


    @staticmethod
    def inserir_categoria(Descrição):
        ct = Categoria(1, Descrição)
        Categorias.inserir(ct)

    @staticmethod
    def listar_categorias():
        return Categorias.listar()
    
    @staticmethod
    def atualizar_categorias(id, Descrição):
        categoria = Categoria(id, Descrição)
        Categorias.atualizar(categoria)

    @staticmethod
    def excluir_categorias(id):
        Categorias.excluir(Categorias.listar_id(id))

    

    @staticmethod
    def inserir_produto(id, Descrição, Preço, Estoque):
        prod = Produto(id, Descrição, Preço, Estoque)
        Produtos.inserir(prod)

    @staticmethod
    def listar_produtos():
       return Produtos.listarProd()
    
    @staticmethod
    def atualizar_produtos(id, descrição, preço, estoque):
        prod = Produto(id, descrição, preço, estoque)
        Produtos.atualizarProd(prod)

    @staticmethod
    def excluir_produtos(id):
        Produtos.excluir(Produtos.listarId(id))