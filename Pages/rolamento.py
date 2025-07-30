import streamlit as st
import math

pg=st.Page("Pages/rolamento.py",title="Lubrificação de Rolamentos",icon="⚙️")
st.title("Lubrificação de Rolamentos ⚙️")

col1,col2,clo3 = st.columns(3)
with col2:
    st.image("Pages/rolamento_img0.png",width=200)
st.markdown("""
        Este aplicativo permite calcular a quantidade de lubrificante necessária para rolamentos.""")

#Formulário para entrada de dados do rolamento
st.header("Informações técnicas do rolamento")
config=st.segmented_control(label="Selecione o tipo de configuração",options=["Pino Descentralizado","Pino Centralizado"],selection_mode="single")
col4,col5 = st.columns(2)

with col4:
    st.markdown("Pino Graxeiro descentralizado")
    st.image("Pages/rolamento_img1.png",width=150)


with col5:
    st.markdown("Pino Graxeiro centralizado")
    st.image("Pages/rolamento_img2.png",width=150)

D=st.number_input("Informe o Diâmetro externo do rolamento (D) em mm ")
B=st.number_input("Informe a Largura do Rolamento (B) em mm")

if st.button("Calcular Quantidade de Graxa"):
    if config is None:
        st.error("Por favor, selecione uma configuração de montagem do rolamento")

    if D<=0 or B<=0:
        st.error("Por favor, insira valores positivos para D e B")

    if config == "Pino Descentralizado":
        Gp = 0.005*D*B
        st.success(f"Relubifique o rolamento com {Gp:.2f} g de Graxa")
        st.warning("Ao finalizar a lubrificação realize a limpeza do pino graxeiro", icon="⚠️")

    if config == "Pino Centralizado":
        Gp = 0.002*D*B
        st.success(f"Relubifique o rolamento com {Gp:.2f} g de Graxa")
        st.warning("Ao finalizar a lubrificação realize a limpeza do pino graxeiro", icon="⚠️")