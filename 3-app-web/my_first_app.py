import streamlit as st

"""
APP SIMPLES PARA DEMONSTRAÇÃO
Este é um exemplo minimalista de Streamlit
Use este arquivo para entender os conceitos básicos antes de ir para o app.py completo
"""

# Configuração da página
st.set_page_config(
    page_title="My First App",
    page_icon="🎯"
)

# Título
st.title("🎯 My First Streamlit App")

# Texto simples
st.write("Olá! Este é um app web feito para a disciplina de Programação com Acesso a Banco de Dados (PABD) desenvolvido com Python e Streamlit!")

# Divisor visual
st.markdown("---")

# Seção 1: Entrada de dados
st.header("1. Entrada de Dados")

nome = st.text_input("Digite seu nome:")
idade = st.number_input("Digite sua idade:", min_value=0, max_value=120, value=18)

# Seção 2: Botão e ação
st.header("2. Interação")

if st.button("Clique aqui!"):
    if nome:
        st.success(f"Olá, {nome}! Você tem {idade} anos.")
        st.balloons()
    else:
        st.warning("Por favor, digite seu nome primeiro!")

# Seção 3: Componentes diversos
st.header("3. Outros Componentes")

col1, col2 = st.columns(2)
with col1:
    cor_favorita = st.selectbox(
        "Sua cor favorita:",
        ["Vermelho", "Azul", "Verde", "Amarelo"]
    )
    st.write(f"Você escolheu: {cor_favorita}")
with col2:
    nota = st.slider("Dê uma nota para este app:", 0, 10, 5)
    st.write(f"Nota: {nota}/10 ⭐")

# Seção 4: Mensagens
st.header("4. Tipos de Mensagens")

st.info("ℹ️ Esta é uma mensagem informativa")
st.success("✅ Esta é uma mensagem de sucesso")
st.warning("⚠️ Esta é uma mensagem de aviso")
st.error("❌ Esta é uma mensagem de erro")

# Rodapé
st.markdown("---")
st.write("Desenvolvido por Raphael Muniz para a disciplina PABD.")
st.markdown("**💡 Dica:** Modifique este código e veja as mudanças em tempo real!")