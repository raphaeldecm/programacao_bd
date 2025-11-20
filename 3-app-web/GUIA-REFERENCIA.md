# 📝 Guia de Referência Rápida - Streamlit

## 🚀 Comandos do Terminal

### Ambiente Virtual
```bash
# Criar ambiente virtual
python3 -m venv venv          # macOS/Linux
python -m venv venv           # Windows

# Ativar ambiente virtual
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows CMD
venv\Scripts\Activate.ps1     # Windows PowerShell

# Desativar ambiente virtual
deactivate
```

### Gerenciamento de Pacotes
```bash
# Instalar Streamlit
pip install streamlit

# Instalar todas as dependências
pip install -r requirements.txt

# Verificar pacotes instalados
pip list

# Verificar versão do Streamlit
streamlit --version

# Criar requirements.txt
pip freeze > requirements.txt
```

### Executar Aplicação
```bash
# Executar app
streamlit run app.py

# Executar em outra porta
streamlit run app.py --server.port 8502

# Executar sem abrir navegador
streamlit run app.py --server.headless true

# Executar app simples
streamlit run my_first_app.py

# Ver ajuda
streamlit --help
```

---

## 🎨 Componentes Streamlit Essenciais

### Texto e Títulos
```python
st.title("Título Principal")
st.header("Cabeçalho")
st.subheader("Subcabeçalho")
st.text("Texto simples")
st.write("Texto com markdown")
st.markdown("**Negrito** e *itálico*")
st.code("print('código')", language="python")
```

### Entrada de Dados
```python
# Texto
texto = st.text_input("Label", placeholder="Digite aqui...")
texto_longo = st.text_area("Texto longo")

# Números
numero = st.number_input("Número", min_value=0, max_value=100, value=50)
slider = st.slider("Slider", 0, 100, 50)

# Seleção
opcao = st.selectbox("Escolha", ["A", "B", "C"])
multiplas = st.multiselect("Múltiplas", ["A", "B", "C"])
radio = st.radio("Radio", ["A", "B", "C"])

# Booleano
check = st.checkbox("Marque aqui")
toggle = st.toggle("Ativar/Desativar")

# Data e Hora
data = st.date_input("Data")
hora = st.time_input("Hora")

# Upload
arquivo = st.file_uploader("Enviar arquivo", type=['csv', 'txt'])
```

### Botões e Ações
```python
# Botão simples
if st.button("Clique aqui"):
    st.write("Clicado!")

# Botão com estilo
if st.button("Importante", type="primary"):
    st.write("Botão primário")

# Download
st.download_button(
    label="Download",
    data="conteúdo",
    file_name="arquivo.txt",
    mime="text/plain"
)
```

### Exibição de Dados
```python
# Texto formatado
st.success("✅ Sucesso!")
st.error("❌ Erro!")
st.warning("⚠️ Aviso!")
st.info("ℹ️ Informação")

# Tabelas
import pandas as pd
df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
st.dataframe(df)
st.table(df)

# Métricas
st.metric("Label", "100", "+10%")

# JSON
st.json({"chave": "valor"})
```

### Layouts
```python
# Colunas
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Coluna 1")

# Abas
tab1, tab2 = st.tabs(["Aba 1", "Aba 2"])
with tab1:
    st.write("Conteúdo da aba 1")

# Expander
with st.expander("Clique para expandir"):
    st.write("Conteúdo oculto")

# Sidebar
with st.sidebar:
    st.title("Menu Lateral")

# Container
with st.container():
    st.write("Conteúdo agrupado")
```

### Formulários
```python
with st.form("meu_form"):
    nome = st.text_input("Nome")
    idade = st.number_input("Idade")
    submitted = st.form_submit_button("Enviar")
    
    if submitted:
        st.write(f"Olá, {nome}!")
```

### Progresso e Carregamento
```python
# Barra de progresso
import time
barra = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    barra.progress(i + 1)

# Spinner
with st.spinner("Carregando..."):
    time.sleep(2)
st.success("Pronto!")

# Status
with st.status("Processando...", expanded=True):
    st.write("Passo 1")
    time.sleep(1)
    st.write("Passo 2")
```

### Gráficos
```python
import pandas as pd

# Dados de exemplo
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [10, 20, 15, 25, 30]
})

# Gráfico de linha
st.line_chart(df)

# Gráfico de barras
st.bar_chart(df)

# Gráfico de área
st.area_chart(df)
```

---

## 🎛️ Configurações

### Configuração da Página
```python
st.set_page_config(
    page_title="Título da Página",
    page_icon="🎯",
    layout="wide",  # ou "centered"
    initial_sidebar_state="expanded"  # ou "collapsed"
)
```

### Cache e Performance
```python
# Cache de dados
@st.cache_data
def carregar_dados():
    return pd.read_csv("dados.csv")

# Cache de recursos (conexões, modelos)
@st.cache_resource
def get_database():
    return Database()
```

### Session State (Estado da Sessão)
```python
# Inicializar
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Usar
st.write(st.session_state.contador)

# Modificar
st.session_state.contador += 1
```

### Rerun (Reexecutar)
```python
# Forçar reexecução da página
st.rerun()
```

---

## 🗄️ Trabalhando com Banco de Dados

### Padrão Básico
```python
import streamlit as st
from models import Database

@st.cache_resource
def get_database():
    return Database("banco.db")

db = get_database()

# Usar db para operações
filmes = db.listar_filmes()
```

### Operações CRUD
```python
# Create
if db.criar_filme(nome, ano, nota):
    st.success("Adicionado!")
    st.rerun()  # Atualizar página

# Read
filmes = db.listar_filmes()
st.dataframe(filmes)

# Update
if db.atualizar_filme(id, nome, ano, nota):
    st.success("Atualizado!")
    st.rerun()

# Delete
if db.deletar_filme(id):
    st.success("Deletado!")
    st.rerun()
```

---

## 🎨 Dicas de Estilo

### Emojis Úteis
```python
# Interface
🎬 🎯 🎨 🎮 🎭 📱 💻 🖥️

# Ações
➕ ✏️ 🗑️ 📋 🔍 🔄 💾 📥 📤

# Status
✅ ❌ ⚠️ ℹ️ 💡 🔔 ⭐ 🏆 

# Navegação
⬅️ ➡️ ⬆️ ⬇️ 🔙 🔜 ▶️ ⏸️

# Dados
📊 📈 📉 📁 📄 📑 📝 🗂️
```

### Markdown
```python
st.markdown("**Negrito**")
st.markdown("*Itálico*")
st.markdown("`código`")
st.markdown("---")  # Linha horizontal
st.markdown("[Link](https://url.com)")
```

### HTML Customizado
```python
st.markdown(
    """
    <div style='text-align: center; color: blue;'>
        <h1>Título Customizado</h1>
    </div>
    """,
    unsafe_allow_html=True
)
```

---

## 🐛 Debugging

### Exibir Valores para Debug
```python
# Mostrar variável
st.write(variavel)

# Mostrar tipo
st.write(type(variavel))

# Mostrar dict/objeto
st.json(dict_ou_objeto)

# Mostrar DataFrame info
st.write(df.dtypes)
st.write(df.shape)
```

### Parar Execução
```python
st.stop()  # Para execução aqui
```

---

## 🔗 Links Úteis

- [Documentação Oficial](https://docs.streamlit.io/)
- [API Reference](https://docs.streamlit.io/library/api-reference)
- [Cheat Sheet](https://cheat-sheet.streamlit.app/)
- [Galeria de Exemplos](https://streamlit.io/gallery)
- [Community Forum](https://discuss.streamlit.io/)
- [30 Days of Streamlit](https://30days.streamlit.app/)

---

## 📋 Checklist de Boas Práticas

- [ ] Usar `st.set_page_config()` como primeira linha
- [ ] Cachear conexões com banco (`@st.cache_resource`)
- [ ] Cachear carregamento de dados (`@st.cache_data`)
- [ ] Usar `st.form()` para agrupar inputs relacionados
- [ ] Adicionar `st.rerun()` após operações de banco
- [ ] Validar inputs do usuário
- [ ] Dar feedback visual (success/error/warning)
- [ ] Usar emojis para melhorar UX
- [ ] Organizar código com funções
- [ ] Adicionar comentários explicativos

---

**Mantenha este guia à mão enquanto desenvolve! 🚀**
