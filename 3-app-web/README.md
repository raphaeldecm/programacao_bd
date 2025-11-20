# Módulo 3: Aplicação Web com Streamlit

## 📖 Objetivo

Neste módulo, você aprenderá a criar uma **aplicação web interativa** usando o **Streamlit**, uma biblioteca Python que permite construir interfaces gráficas modernas de forma simples e rápida.

Vamos migrar nosso sistema de filmes do console para uma interface web visual e intuitiva!

**Consulta da Documentação:** https://docs.streamlit.io/develop/api-reference

## 🎯 Conceitos Abordados

- **Criação de ambiente virtual Python**
- **Instalação e uso do Streamlit**
- **Componentes de interface (inputs, buttons, tabelas)**
- **Formulários web**
- **Gerenciamento de estado da aplicação**
- **CRUD completo com interface gráfica**
- **Feedback visual para o usuário**

## 🌟 Por que Streamlit?

- ✅ **Fácil de aprender** - Código Python puro, sem HTML/CSS/JavaScript
- ✅ **Rápido de desenvolver** - Protótipos em minutos
- ✅ **Interface moderna** - Design responsivo e profissional
- ✅ **Interativo** - Atualização automática da página
- ✅ **Ideal para dados** - Perfeito para aplicações com banco de dados

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter:
- Python 3.7 ou superior instalado
- Conhecimento básico de Python e SQLite
- Ter concluído os módulos anteriores (1-integracao e 2-aplicacao-console)

---

## 🚀 Passo 1: Configurando o Ambiente Virtual

### O que é um Ambiente Virtual?

Um **ambiente virtual** é um espaço isolado para instalar bibliotecas Python específicas do seu projeto, sem afetar outros projetos ou o sistema.

**Vantagens:**
- Evita conflitos entre versões de bibliotecas
- Mantém o projeto organizado e portátil
- Facilita o compartilhamento com outras pessoas

### Criando o Ambiente Virtual

Abra o terminal na pasta `3-app-web` e execute:

```bash
# No Windows
python -m venv venv

# No macOS/Linux
python3 -m venv venv
```

Isso criará uma pasta `venv` com o ambiente isolado.

### Ativando o Ambiente Virtual

Sempre que for trabalhar no projeto, ative o ambiente:

```bash
# No Windows (cmd)
venv\Scripts\activate

# No Windows (PowerShell)
venv\Scripts\Activate.ps1

# No macOS/Linux
source venv/bin/activate
```

Você verá `(venv)` no início da linha do terminal, indicando que está ativo.

### Desativando o Ambiente (quando terminar)

```bash
deactivate
```

---

## 📦 Passo 2: Instalando o Streamlit

Com o ambiente virtual **ativado**, instale o Streamlit:

```bash
pip install streamlit
```

Para verificar se a instalação foi bem-sucedida:

```bash
streamlit --version
```

Você também pode testar o Streamlit com um exemplo:

```bash
streamlit hello
```

Isso abrirá uma demonstração no navegador mostrando as capacidades do Streamlit.

---

## 📁 Passo 3: Estrutura do Projeto

Nosso módulo terá a seguinte estrutura:

```
3-app-web/
├── venv/                    # Ambiente virtual (não versionar)
├── models.py                # Classe Database (reutilizada do módulo 2)
├── app.py                   # Aplicação Streamlit completa
├── my_first_app.py           # Exemplo simples para iniciantes
├── filmes.db                # Banco de dados SQLite (criado automaticamente)
├── requirements.txt         # Dependências do projeto
├── .gitignore               # Arquivos a ignorar no Git
├── README.md                # Documentação completa (este arquivo)
├── INICIO-RAPIDO.md         # Guia rápido de 5 minutos
├── EXERCICIOS.md            # Lista de exercícios práticos
└── PLANO-DE-AULA.md         # Plano de aula para professores
```

### 📄 Descrição dos Arquivos

**Para Alunos:**
- `INICIO-RAPIDO.md` - Comece por aqui! Guia rápido para rodar a aplicação
- `my_first_app.py` - Exemplo minimalista para aprender os conceitos básicos
- `app.py` - Aplicação completa do sistema de filmes
- `EXERCICIOS.md` - Exercícios para praticar (do básico ao avançado)

**Para Professores:**
- `PLANO-DE-AULA.md` - Planejamento completo da aula com roteiro e dicas

**Arquivos Técnicos:**
- `models.py` - Classe para gerenciar o banco de dados
- `requirements.txt` - Lista de bibliotecas necessárias
- `.gitignore` - Configuração do Git

---

## 🔧 Passo 4: Preparando o Código

### 4.1 - Copiando a Classe Database

Primeiro, vamos copiar o arquivo `models.py` do módulo anterior:

```bash
# Execute na pasta 3-app-web
cp ../2-aplicacao-console/models.py .
```

Ou copie manualmente o arquivo `models.py` do módulo 2 para esta pasta.

### 4.2 - Criando o arquivo requirements.txt

Crie um arquivo `requirements.txt` para documentar as dependências:

```txt
streamlit==1.29.0
```

**Dica:** Qualquer pessoa pode instalar todas as dependências com:
```bash
pip install -r requirements.txt
```

---

## 💻 Passo 5: Criando a Aplicação Streamlit

Agora vamos criar o arquivo `app.py` com nossa interface web!

### 5.1 - Estrutura Básica

```python
import streamlit as st
from models import Database

# Configuração da página
st.set_page_config(
    page_title="Sistema de Filmes",
    page_icon="🎬",
    layout="wide"
)

# Título principal
st.title("🎬 Sistema de Gerenciamento de Filmes")
```

### 5.2 - Inicializando o Banco de Dados

```python
# Inicializar a conexão com o banco
@st.cache_resource
def get_database():
    return Database("filmes.db")

db = get_database()
```

**Explicação:**
- `@st.cache_resource`: Mantém a mesma conexão durante toda a sessão, evitando reconexões

### 5.3 - Componentes Principais do Streamlit

#### Entrada de Texto
```python
nome = st.text_input("Nome do filme")
```

#### Entrada Numérica
```python
ano = st.number_input("Ano", min_value=1900, max_value=2030, value=2024)
```

#### Slider
```python
nota = st.slider("Nota", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
```

#### Botão
```python
if st.button("Adicionar Filme"):
    # código executado quando o botão é clicado
    pass
```

#### Exibir Mensagens
```python
st.success("Filme adicionado com sucesso!")
st.error("Erro ao adicionar filme!")
st.warning("Atenção!")
st.info("Informação importante")
```

#### Exibir Tabelas
```python
import pandas as pd

filmes = db.listar_filmes()
df = pd.DataFrame(filmes, columns=["ID", "Nome", "Ano", "Nota"])
st.dataframe(df)
```

### 5.4 - Organizando com Abas

```python
tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Adicionar", 
    "📋 Listar", 
    "✏️ Atualizar", 
    "🗑️ Deletar"
])

with tab1:
    st.header("Adicionar Novo Filme")
    # código para adicionar

with tab2:
    st.header("Lista de Filmes")
    # código para listar
```

---

## 📝 Passo 6: Implementação Completa

### Código Completo do `app.py`

Aqui está a implementação completa do sistema:

```python
import streamlit as st
import pandas as pd
from models import Database

# Configuração da página
st.set_page_config(
    page_title="Sistema de Filmes",
    page_icon="🎬",
    layout="wide"
)

# Inicializar banco de dados
@st.cache_resource
def get_database():
    return Database("filmes.db")

db = get_database()

# Título principal
st.title("🎬 Sistema de Gerenciamento de Filmes")
st.markdown("---")

# Criar abas para diferentes operações
tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Adicionar Filme", 
    "📋 Listar Filmes", 
    "✏️ Atualizar Filme", 
    "🗑️ Deletar Filme"
])

# TAB 1: Adicionar Filme
with tab1:
    st.header("Adicionar Novo Filme")
    
    with st.form("form_adicionar"):
        nome = st.text_input("Nome do Filme", placeholder="Ex: Inception")
        col1, col2 = st.columns(2)
        
        with col1:
            ano = st.number_input(
                "Ano de Lançamento", 
                min_value=1900, 
                max_value=2030, 
                value=2024
            )
        
        with col2:
            nota = st.slider(
                "Nota (0.0 a 10.0)", 
                min_value=0.0, 
                max_value=10.0, 
                value=5.0, 
                step=0.1
            )
        
        submitted = st.form_submit_button("Adicionar Filme", use_container_width=True)
        
        if submitted:
            if not nome.strip():
                st.error("❌ O nome do filme não pode estar vazio!")
            else:
                if db.criar_filme(nome, ano, nota):
                    st.success(f"✅ Filme '{nome}' adicionado com sucesso!")
                    st.balloons()
                else:
                    st.error("❌ Erro ao adicionar filme!")

# TAB 2: Listar Filmes
with tab2:
    st.header("Lista de Filmes")
    
    # Botão para recarregar
    if st.button("🔄 Recarregar Lista"):
        st.rerun()
    
    filmes = db.listar_filmes()
    
    if not filmes:
        st.info("📭 Nenhum filme cadastrado ainda. Adicione um filme na primeira aba!")
    else:
        # Converter para DataFrame do pandas
        df = pd.DataFrame(filmes, columns=["ID", "Nome", "Ano", "Nota"])
        
        # Estatísticas
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Filmes", len(filmes))
        with col2:
            st.metric("Nota Média", f"{df['Nota'].mean():.2f}")
        with col3:
            st.metric("Melhor Nota", f"{df['Nota'].max():.1f}")
        
        st.markdown("---")
        
        # Exibir tabela
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "ID": st.column_config.NumberColumn("ID", width="small"),
                "Nome": st.column_config.TextColumn("Nome do Filme", width="large"),
                "Ano": st.column_config.NumberColumn("Ano", width="small"),
                "Nota": st.column_config.NumberColumn(
                    "Nota",
                    format="%.1f ⭐",
                    width="small"
                )
            }
        )

# TAB 3: Atualizar Filme
with tab3:
    st.header("Atualizar Filme")
    
    filmes = db.listar_filmes()
    
    if not filmes:
        st.info("📭 Nenhum filme cadastrado para atualizar.")
    else:
        # Criar dicionário de filmes para seleção
        filmes_dict = {f"{filme[0]} - {filme[1]}": filme[0] for filme in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para atualizar",
            options=list(filmes_dict.keys())
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = db.buscar_filme_por_id(filme_id)
            
            if filme_atual:
                st.markdown(f"**Filme atual:** {filme_atual[1]} ({filme_atual[2]}) - Nota: {filme_atual[3]}")
                
                with st.form("form_atualizar"):
                    novo_nome = st.text_input("Novo Nome", value=filme_atual[1])
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        novo_ano = st.number_input(
                            "Novo Ano", 
                            min_value=1900, 
                            max_value=2030, 
                            value=int(filme_atual[2])
                        )
                    with col2:
                        nova_nota = st.slider(
                            "Nova Nota", 
                            min_value=0.0, 
                            max_value=10.0, 
                            value=float(filme_atual[3]), 
                            step=0.1
                        )
                    
                    submitted = st.form_submit_button("Atualizar Filme", use_container_width=True)
                    
                    if submitted:
                        if not novo_nome.strip():
                            st.error("❌ O nome do filme não pode estar vazio!")
                        else:
                            if db.atualizar_filme(filme_id, novo_nome, novo_ano, nova_nota):
                                st.success(f"✅ Filme atualizado com sucesso!")
                                st.rerun()
                            else:
                                st.error("❌ Erro ao atualizar filme!")

# TAB 4: Deletar Filme
with tab4:
    st.header("Deletar Filme")
    
    filmes = db.listar_filmes()
    
    if not filmes:
        st.info("📭 Nenhum filme cadastrado para deletar.")
    else:
        filmes_dict = {f"{filme[0]} - {filme[1]}": filme[0] for filme in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para deletar",
            options=list(filmes_dict.keys()),
            key="delete_select"
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = db.buscar_filme_por_id(filme_id)
            
            if filme_atual:
                st.warning(f"⚠️ Você está prestes a deletar: **{filme_atual[1]} ({filme_atual[2]})**")
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    if st.button("🗑️ Confirmar Exclusão", type="primary"):
                        if db.deletar_filme(filme_id):
                            st.success("✅ Filme deletado com sucesso!")
                            st.rerun()
                        else:
                            st.error("❌ Erro ao deletar filme!")

# Rodapé
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>💡 Sistema desenvolvido com Streamlit | 📚 Programação com Banco de Dados</p>
    </div>
    """,
    unsafe_allow_html=True
)
```

---

## 🎮 Passo 7: Executando a Aplicação

### Iniciar o Servidor Streamlit

No terminal, com o ambiente virtual ativado, execute:

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`

### Comandos Úteis

```bash
# Parar o servidor: Ctrl + C

# Executar em outra porta
streamlit run app.py --server.port 8502

# Abrir sem abrir o navegador automaticamente
streamlit run app.py --server.headless true
```

---

## 🔍 Entendendo os Componentes

### Forms (Formulários)

Formulários agrupam inputs e só enviam dados quando o botão é clicado:

```python
with st.form("meu_form"):
    nome = st.text_input("Nome")
    submitted = st.form_submit_button("Enviar")
    
    if submitted:
        # processar dados
        pass
```

### Session State (Estado da Sessão)

Para manter dados entre recarregamentos:

```python
if 'contador' not in st.session_state:
    st.session_state.contador = 0

if st.button("Incrementar"):
    st.session_state.contador += 1

st.write(f"Contador: {st.session_state.contador}")
```

### Layouts

```python
# Colunas
col1, col2, col3 = st.columns(3)
with col1:
    st.write("Coluna 1")

# Sidebar
with st.sidebar:
    st.title("Menu Lateral")

# Expander (seção expansível)
with st.expander("Clique para expandir"):
    st.write("Conteúdo oculto")
```

---

## 🎨 Personalizando a Aplicação

### Temas

Streamlit suporta temas claro e escuro. Configure em `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

### Ícones e Emojis

Use emojis para deixar a interface mais amigável:

```python
st.title("🎬 Meu Título")
st.button("✅ Confirmar")
st.error("❌ Erro!")
```

[Lista de emojis](https://emojipedia.org/)

---

## 📚 Comparação: Console vs Web

| Aspecto | Console (Módulo 2) | Web (Módulo 3) |
|---------|-------------------|----------------|
| Interface | Texto no terminal | Interface gráfica no navegador |
| Entrada de dados | `input()` | Widgets visuais |
| Exibição | `print()` | Componentes ricos (tabelas, gráficos) |
| Usabilidade | Apenas desenvolvedores | Qualquer usuário |
| Visual | Simples | Moderno e profissional |
| Curva de aprendizado | Baixa | Baixa (com Streamlit) |

---

## 🐛 Problemas Comuns e Soluções

### 1. Página não atualiza após mudanças no banco

**Solução:** Use `st.rerun()` após operações de banco:
```python
if db.criar_filme(nome, ano, nota):
    st.success("Adicionado!")
    st.rerun()  # Recarrega a página
```

### 2. "ModuleNotFoundError: No module named 'streamlit'"

**Solução:** Ative o ambiente virtual e instale o Streamlit:
```bash
source venv/bin/activate  # macOS/Linux
pip install streamlit
```

### 3. Dados duplicando ao clicar várias vezes

**Solução:** Use `st.form()` para prevenir múltiplos envios.

### 4. Aplicação lenta com muitos dados

**Solução:** Use `st.cache_data` para cachear consultas:
```python
@st.cache_data
def listar_todos_filmes():
    return db.listar_filmes()
```

---

## 🎯 Exercícios Práticos

### Exercício 1: Filtro de Busca
Adicione um campo de busca na aba "Listar Filmes" para filtrar por nome.

### Exercício 2: Ordenação
Adicione opções para ordenar a lista por nome, ano ou nota.

### Exercício 3: Gráficos
Use `st.bar_chart()` para criar um gráfico de filmes por ano.

### Exercício 4: Validações Avançadas
Impeça a adição de filmes duplicados (mesmo nome e ano).

### Exercício 5: Export
Adicione um botão para exportar a lista de filmes em CSV.

**Dica para o exercício 5:**
```python
import pandas as pd

df = pd.DataFrame(filmes, columns=["ID", "Nome", "Ano", "Nota"])
csv = df.to_csv(index=False)
st.download_button("Download CSV", csv, "filmes.csv", "text/csv")
```

---

## 📖 Recursos Adicionais

### Documentação Oficial
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Streamlit Cheat Sheet](https://cheat-sheet.streamlit.app/)
- [Streamlit Gallery](https://streamlit.io/gallery)

### Tutoriais
- [30 Days of Streamlit](https://30days.streamlit.app/)
- [Streamlit YouTube Channel](https://www.youtube.com/@streamlitofficial)

---

## 🚀 Próximos Passos

No **Módulo 4**, você aprenderá sobre **SQLAlchemy ORM**, que permite trabalhar com banco de dados de forma ainda mais orientada a objetos, sem escrever SQL diretamente!

---

## 💡 Dicas Finais

1. **Sempre ative o ambiente virtual** antes de trabalhar no projeto
2. **Use `st.rerun()`** para atualizar a página após operações no banco
3. **Teste cada funcionalidade** antes de adicionar a próxima
4. **Leia as mensagens de erro** - elas geralmente indicam o problema
5. **Consulte a documentação** do Streamlit quando tiver dúvidas
6. **Experimente** - Streamlit é fácil de testar e modificar!

---

**Bons estudos e divirta-se criando aplicações web! 🚀**