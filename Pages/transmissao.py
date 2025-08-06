import streamlit as st
import numpy as np
from fractions import Fraction
import plotly.express as px

st.title("Relação de Transmissão - Correias")
st.image("Pages/correiais_img.png", width=1500)

st.write("Dados da Polia Motora:")
d=st.number_input("Insira o Diâmetro da Polia Motora em mm",min_value=1,value=100)
D=st.number_input("Insira o Diâmetro da Polia Movida em mm",min_value=1,value=200)
n=st.number_input("Informe a rotação do motor em RPM",min_value=1,value=1500)

#Relação de transmissão
#nd=ND -> N=nd/D
if st.button("Realizar Cálculo"):
    if d<=0 or D<=0 or n<=0:
        st.error("Insira valores válidos")
    N=n*d/D
    ratio_transm=Fraction(int(N),int(n))
    diametros=np.linspace(d,D,100)
    Ngrafico=n*d/diametros
    st.success(f"A rotação da polia movida é de {N:.2f} RPM")
    st.success(f"A relação de transmissão é de {ratio_transm}")
    fig=px.line(x=diametros,y=Ngrafico,labels={"x": "Diâmetro da polia movida (mm)",
                "y": "Rotação da polia movida (RPM)"},
                title="Relação da Rotação da Polia Movida em função do Diâmetro",
                markers=True)
    st.plotly_chart(fig)
    