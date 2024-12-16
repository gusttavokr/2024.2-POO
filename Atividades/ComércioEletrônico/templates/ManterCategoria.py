import streamlit as st
import pandas as p
from View import View
import time

class ManterCategoria:
    def main():
        st.header("Cadastro de Categorias")
        t1, t2, t3, t4 = st.tabs(["Inserir", "Listar", "Atualizar", "Excluir"])
        with t1 : ManterCategoria.inserir()
        with t2 : ManterCategoria.listar()
        with t3 : ManterCategoria.atualizar()
        with t4 : ManterCategoria.excluir()

    def inserir():
        descrição = st.text_input("Informe a descrição da nova categoria:")

        if st.button("Cadastrar"):
            View.inserir_categoria(descrição)
            st.success("Categoria cadastrada com sucesso")
            time.sleep(2)
            st.rerun()

    def listar():
        categorias = View.listar_categorias()

        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            dic = []
            for obj in categorias:
                dic.append(obj.__dict__)
            df = p.DataFrame(dic)
            st.dataframe(df)

    def atualizar():
        categorias = View.listar_categorias()
    
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Atualização das categorias", categorias)
            descrição = st.text_input("Informe a nova descrição da categoria:", op.getDesc())

        if st.button("Atualizar"):
            View.atualizar_categorias(op.getId(), descrição)
            st.success("Categoria atualizada com sucesso")
            time.sleep(2)
            st.rerun()

    def excluir():
        categorias = View.listar_categorias()

        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            op = st.selectbox("Excluir categoria", categorias)
            if st.button("Excluir"):
                View.excluir_categorias(op.getId())
                st.success("Categoria excluída com sucesso!")
                time.sleep(2)
                st.rerun()