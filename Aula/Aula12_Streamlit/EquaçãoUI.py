import streamlit as st
from Equação import Equação
import pandas as pd

class EquaçãoUI:
    def main():
        st.header("Equação de II Grau: y = ax² + bx + c")
        a = st.text_input("Informe A:")
        b = st.text_input("Informe B:")
        c = st.text_input("Informe C:")
        n = st.text_input("Informe o número de pontos do gráfico:")

        if st.button("Calcular"):
            e = Equação(float(a), float(b), float(c))
            st.write(e)
            delta = e.delta()
            st.write(f"Delta = {delta}")

            x1 = e.x1(delta)
            st.write(f"X1 = {x1}")

            x2 = e.x2(delta)
            st.write(f"X2 = {x2}")

            px = [] # Coordenada de x de vários pontos
            py = [] # Coordenada de y de vários pontos


            if delta > 0:
                d = x2 - x1
                xmin = x1 - d/2 # Limite inferior do gráfico
                xmax = x2 + d/2 # Limite superior do gráfico

            if delta == 0:
                xmin = 0.5 * x1 # Limite inferior do gráfico
                xmax = 1.5 * x1
            
            if delta < 0:
                xmin = 0.5*e.xplano()
                xmax = 1.5*e.xplano()

            if xmin == 0 and xmax == 0:
                xmin = -5
                xmax = 5

            n_pontos = int(n)
            d = (xmax-xmin)/n_pontos
            x = xmin

            while x < xmax:
                px.append(x)
                py.append(e.Y(x))
                x += d
            px.append(xmax)
            py.append(e.Y(xmax))
            #st.write(px)
            #st.write(py)
            dic = {"x" : px, "y" : py}
            chart_data = pd.DataFrame(dic)
            st.line_chart(chart_data, x = "x", y = "y")


            #st.line_chart()
            
