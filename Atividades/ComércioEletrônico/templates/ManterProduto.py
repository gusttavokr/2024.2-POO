from View import View
import streamlit as st
import pandas as p
import time
from templates.ManterCategoria import ManterCategoria

class ManterProduto:
    def main():
        st.header("Cadastro de Produtos")
        t1, t2, t3, t4, t5 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir", "Reajustar"])
        with t1: 
            ManterProduto.inserir()
        with t2:
            ManterProduto.listar()
        with t3:
            ManterProduto.atualizar()
        with t4:
            ManterProduto.excluir()
        with t5:
            ManterProduto.reajustar()
    @classmethod
    def inserir(cls):
        descrição = st.text_input("Insira a descrição do produto: ")
        preço = st.number_input("Insira o preço do produto: ")
        estoque = st.number_input("Insira o estoque do produto: ", value=0, step=1)
        ManterCategoria.listar()
        categorias = View.listar_categorias()
        id_categoria = st.selectbox("Selecione a categoria do produto:", categorias)

        # for i in categorias:
        #     if i == id_categoria:
        #         id_categoria = i.getDesc()

        # for i in categorias:
        #     if i == id_categoria.getDesc():
        #         id_categoria = i.getDesc()
            
        id_categoria = id_categoria.getDesc()    

        if st.button("Inserir"):
            View.inserir_produto(1, descrição, preço, estoque, id_categoria)
            st.success("Produto inserido com sucesso!")
            time.sleep(2)
            st.rerun()

            #return id_categoria
        # if len(categorias) == 0:
        #     st.write("Nenhuma categoria cadastrada")
        # else:
            # categoria = None
        # for i in categorias:
        #     if i.getId() == id_categoria:
        #         categoria = i.getDesc()
        #     return categoria
        

        

    def listar():
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            dic = []
            for obj in produtos:
                dic.append(obj.__dict__)
            df = p.DataFrame(dic)
            st.dataframe(df)

    @classmethod
    def atualizar(cls):
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de produtos", produtos)
            op = op.getId()
            descrição = st.text_input("Insira a nova descrição: ")
            preço = st.number_input("Insira o novo preço: ")
            estoque = st.number_input("Insira o novo estoque: ", value = 0, step = 1)
            ManterCategoria.listar()
            categorias = View.listar_categorias()
            op2 = st.selectbox("Selecione a categoria do produto: ", categorias)
            op2 = op2.getDesc()

            if st.button("Atualizar"):
                View.atualizar_produtos(op, descrição, preço, estoque, op2)
                st.success("Produto atualizado com sucesso!")
                time.sleep(2)
                st.rerun()

    def excluir():
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Excluir produto", produtos)
            if st.button("Excluir"):
                View.excluir_produtos(op.getId())
                st.success("Produto excluído com sucesso")
                time.sleep(2)
                st.rerun()

    def reajustar():
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            reajuste = st.number_input("Informe o percentual de reajuste %: ", value =0, step =1)
            if st.button("Reajustar produto"):
                View.produto_reajustar(reajuste/100)
                st.success("Reajuste realizado com sucesso")
                time.sleep(2)
                st.rerun()

    # @staticmethod
    # def desc(categorias, id_categoria):
    #     for i in categorias:
    #         if i == id_categoria:
    #             id_categoria = i.getDesc()
    #             return id_categoria