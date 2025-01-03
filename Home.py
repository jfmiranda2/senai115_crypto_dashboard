import streamlit as st
import pandas as pd
import numpy as np


long_text = "Lorem ipsum. " * 1000

st.title('projeto criptomoeda!')

#Noticias mundo cripto



#Listar as moedas favoritas
options = st.multiselect(
    "Selecione as moedas do teu interesse",
    ["BTC", "ETH", "SOL"],
    ["BTC"],
)

for option in options:
    print(option)
    with st.container(height=300):
        st.markdown(option)

