import streamlit as st
from retangulo import Retangulo

class RetanguloUI:
    # @staticmethod
    def main():
        st.header("Cálculo com Retângulo")
        b = st.text_input("Informe a base: ")
        a = st.text_input("Informe a altura: ")
        if (st.button("Calcular")):
            r = Retangulo(float(b), float(a))
            st.write(r)
            st.write(f"Área = {r.calc_area()}")
            st.write(f"Diagonal = {r.calc_diagonal()}")
