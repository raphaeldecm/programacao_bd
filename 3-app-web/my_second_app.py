import streamlit as st
import pandas as pd

"""
APP SIMPLES PARA DEMONSTRAÇÃO
Este é um exemplo minimalista de Streamlit retirado da documentação oficial. https://streamlit.io/
Use este arquivo para entender os conceitos básicos antes de ir para o app.py completo
"""

st.write("""
  # My second Streamlit App
  Hello *world*! This is my second app built with Streamlit.
""")

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
st.line_chart(df)