import streamlit as st
import numpy as np
from fractions import Fraction
import matplotlib.pyplot as plt

st.title("Relação de Transmissão - Correias")
st.image("Pages/correiais_img.png", width=1500)

st.write("Dados da Polia Motora:")
d=st.number_input("Insira o Diâmetro da Polia Motora em mm")
D=st.number_input("Insira o Diâmetro da Polia Movida em mm")
n=st.number_input("Informe a rotação do motor em RPM")

#Relação de transmissão
#nd=ND -> N=nd/D
if st.button("Realizar Cálculo"):
    if d<=0 or D<=0 or n<=0:
        st.error("Insira valores válidos")
    N=n*d/D
    ratio_transm=Fraction(int(N),int(n))
    diametros=np.linspace(d,D,100)
    Ngrafico=n*d/diametros
    st.success(f"A rotação da polia movida é de {N} RPM")
    st.success(f"A relação de transmissão é de {ratio_transm}")
    fig,ax = plt.subplots()
    ax.plot(diametros,Ngrafico)
    ax.set_xlabel("Diâmetro da polia movida (mm)")
    ax.set_ylabel("Rotação da polia movida (RPM)")
    ax.set_title("Relação da Rotação da Polia Mov. em função do diâmetro")
    st.pyplot(fig)
    