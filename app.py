import streamlit as st
import math

#st.set_page_config(page_title="Calculadoras de Engenharia",page_icon="⚙️",layout="wide",initial_sidebar_state="expanded")
#st.title("Calculadoras de Engenharia ⚙️")

pages = {"Calculadoras de Engenharia":
    [st.Page("Pages/correiais.py", title="Dimensionamento de Correias", icon="⚙️"),
    st.Page("Pages/rolamento.py", title="Lubrificação de Rolamentos", icon="⚙️"),
]}

pg=st.navigation(pages)
pg.run()