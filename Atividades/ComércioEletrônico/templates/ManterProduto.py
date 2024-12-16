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
        # with t5:
        #     ManterProduto.reajustar()
        
    def inserir():
        descrição = st.text_input("Insira a descrição do produto: ")
        preço = st.number_input("Insira o preço do produto: ")
        estoque = st.number_input("Insira o estoque do produto: ", value=0, step=1)
        ManterCategoria.listar()
        categorias = View.listar_categorias()
        id_categoria = st.selectbox("Selecione a categoria do produto:", categorias)

        if st.button("Inserir"):
            View.inserir_produto(1, descrição, preço, estoque, id_categoria)
            st.success("Produto inserido com sucesso!")
            time.sleep(2)
            st.rerun()

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

    def atualizar():
        produtos = View.listar_produtos()
        if len(produtos) == 0:
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de produtos", produtos)
            descrição = st.text_input("Insira a nova descrição: ")
            preço = st.number_input("Insira o novo preço: ")
            estoque = (st.number_input("Insira o novo estoque: "))
            id = st.number_input("Insira o id da categoria do novo produto: ")

            if st.button("Atualizar"):
                View.atualizar_produtos(op, descrição, preço, estoque, id)
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
