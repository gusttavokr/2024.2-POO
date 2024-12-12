from Models.Cliente import Cliente, Clientes
from Models.Categoria import Categoria, Categorias
from Models.Produto import Produto, Produtos

class View:

    @staticmethod
    def cliente_admin():
        for c in Clientes.listar():
            if c.getEmail() == "admin":
                return None
        View.inserir_cliente("admin", "admin", "0000", "1234")

    @staticmethod
    def cliente_autenticar():
        for c in Clientes.listar():
            if c.getEmail() == "email" and c.getSenha() == "senha":
                return { "id" : c.id, "nome" : c.nome }
        return None


    @staticmethod
    def inserir_cliente(nome, email, fone, senha):
        cliente = Cliente(1, nome, email, fone, senha) 
        Clientes.inserir(cliente)

    @staticmethod
    def listar_clientes():
        return Clientes.listar()
    
    @staticmethod
    def atualizar_clientes(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        Clientes.atualizar(cliente) # Usando o método atualizar na variável cliente

    @staticmethod
    def excluir_clientes(id):
        c = Cliente(id, "", "", "", "")
        Clientes.excluir(c)

    


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
    def inserir_produto(id, Descrição, Preço, Estoque, id_categoria):
        prod = Produto(id, Descrição, Preço, Estoque, id_categoria)
        Produtos.inserir(prod)

    @staticmethod
    def listar_produtos():
       return Produtos.listarProd()
    
    @staticmethod
    def atualizar_produtos(id, descrição, preço, estoque, id_categoria):
        prod = Produto(id, descrição, preço, estoque, id_categoria)
        Produtos.atualizarProd(prod)

    @staticmethod
    def excluir_produtos(id):
        Produtos.excluir(Produtos.listarId(id))

    @staticmethod
    def produto_reajustar(percentual):
        for obj in View.listar_produtos():
            View.atualizar_produtos(obj.getId(), obj.getDesc(), obj.getPreço() * (1 + percentual), obj.getEstoque(), obj.getId_Categoria())