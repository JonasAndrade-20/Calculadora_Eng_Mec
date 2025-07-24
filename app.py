import streamlit as st
import math

st.set_page_config(page_title="Dimensionamento de Correiais",page_icon="⚙️",layout="wide")   
st.title("Dimensionamento de Correiais ⚙️")
st.image("correiais_img.png", width=1500)
st.markdown("""
    Este aplicativo permite calcular o comprimento de correias para polias motora e movida.
    Insira os diâmetros das polias e a distância entre os centros para obter o comprimento da correia.
""")
# Inserindo dados de entrada das informações das polias
st.header("Dados das Polias")
D=st.number_input(label="Insira o Diâmetro da polia Movida (D) em mm")
d=st.number_input(label="Insira o Diâmetro da polia Motora (d) em mm")
c=st.number_input(label="Insira a Distância entre os centros das polias (c) em mm")


# Inserindo um botão para calcular o comprimento das correias
if st.button(label="Calcular o comprimento das correias"):
    #Calculando o comprimento das correias
    if D <= 0 or d <= 0 or c <= 0:
        st.error("Por favor, insira valores positivos para D, d e c.")
    else:
        L=2*c + math.pi*(D+d)/2 + ((D-d)**2)/(4*c)
        st.success(f"O comprimento da correia deve ser de: {L:.2f} mm")

