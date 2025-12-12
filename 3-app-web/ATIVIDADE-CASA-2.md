# 🏠 Atividade para Casa 2 - Estruturando um Sistema com Tabs

## 📋 Informações da Atividade

**Objetivo:** Criar a estrutura visual de um sistema CRUD usando tabs (abas) do Streamlit  
**Pré-requisito:** Atividade para Casa 1 concluída  
**Consulta da Documentação:** https://docs.streamlit.io/develop/api-reference

---

## 🎯 Objetivo

Criar a **interface visual** de um Sistema de Cadastro de Livros usando **tabs** (abas) do Streamlit. Nesta atividade, você vai estruturar as 4 páginas principais de um sistema CRUD, mas **SEM implementar as funcionalidades** ainda.

> **Importante:** Esta atividade foca apenas na **aparência e organização** das páginas. As funcionalidades de salvar, listar, atualizar e deletar serão implementadas em uma próxima atividade!

---

## 📝 O que você deve fazer

Crie um arquivo chamado `sistema_livros.py` com as seguintes características:

### Estrutura Geral

1. **Título principal** do sistema
2. **Linha divisória** visual
3. **Quatro tabs (abas)** com os nomes:
   - 📚 Cadastrar
   - 📖 Listar
   - ✏️ Atualizar
   - 🗑️ Deletar

**Exemplo de código base:**
```python
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Sistema de Livros",
    page_icon="📚",
    layout="wide"
)

# Título principal
st.title("📚 Sistema de Cadastro de Livros")
st.markdown("---")

# Criar as tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Cadastrar", "📖 Listar", "✏️ Atualizar", "🗑️ Deletar"])

# Conteúdo de cada tab
with tab1:
    # Código da aba Cadastrar
    pass

with tab2:
    # Código da aba Listar
    pass

with tab3:
    # Código da aba Atualizar
    pass

with tab4:
    # Código da aba Deletar
    pass
```

---

## 📑 Tab 1: Cadastrar

### O que deve ter:

1. **Subtítulo:** "Cadastrar Novo Livro"
2. **Formulário** com os seguintes campos:
   - **Título do livro** (text_input)
   - **Autor** (text_input)
   - **Ano de publicação** (number_input, de 1500 a 2025)
   - **Gênero** (selectbox com opções: Ficção, Romance, Terror, Fantasia, Biografia, Técnico, Infantil)
   - **Número de páginas** (number_input, mínimo 1)
   - **Nota** (slider de 0.0 a 10.0, com incremento de 0.5)
3. **Botão** "Cadastrar Livro"
4. **Mensagem informativa** (info) explicando que a funcionalidade será implementada depois

---

## 📑 Tab 2: Listar

### O que deve ter:

1. **Subtítulo:** "Lista de Livros Cadastrados"
2. **Mensagem informativa** explicando que a listagem será implementada depois
3. **Exemplo visual** de como os livros serão exibidos (use `st.write()` para simular)

---

## 📑 Tab 3: Atualizar

### O que deve ter:

1. **Subtítulo:** "Atualizar Livro"
2. **Campo de seleção** para escolher qual livro atualizar:
   - Use um `selectbox` com alguns exemplos simulados
3. **Formulário** com os mesmos campos da aba Cadastrar
4. **Botão** "Salvar Alterações"
5. **Mensagem informativa** explicando que a funcionalidade será implementada depois

---

## 📑 Tab 4: Deletar

### O que deve ter:

1. **Subtítulo:** "Deletar Livro"
2. **Campo de seleção** para escolher qual livro deletar
3. **Área de aviso** (`st.warning()`) alertando sobre a ação
4. **Botão de confirmação** "Confirmar Exclusão" (use `type="primary"` para destacar)
5. **Mensagem informativa** explicando que a funcionalidade será implementada depois

---

## 🌟 Desafios Extras - BÔNUS

### Bônus 1: Rodapé Estilizado

Adicione um rodapé ao final da página com informações do sistema:

### Bônus 2: Sidebar com Informações

Adicione uma barra lateral com instruções:

### Bônus 3: Colunas na Tab Listar

Na tab "Listar", organize a prévia em colunas usando `st.columns()`:


### Bônus 4: Ícones e Emojis

Use emojis e ícones de forma criativa em todos os textos e botões para deixar a interface mais atrativa.

---

## 📸 Como Entregar

1. Salve seu arquivo `sistema_livros.py`
2. Tire **4 screenshots** (um de cada tab funcionando)
3. Crie um arquivo `PRINTS.txt` listando o que cada imagem mostra
4. Envie:
   - `sistema_livros.py`
   - As 4 imagens (pode ser PNG ou JPG)
   - `PRINTS.txt`

**Exemplo de PRINTS.txt:**
```
print1.png - Tab Cadastrar com todos os campos
print2.png - Tab Listar com a prévia
print3.png - Tab Atualizar com campos preenchidos
print4.png - Tab Deletar com mensagem de aviso
```

---

## 🐛 Problemas Comuns

### Erro: "DuplicateWidgetID"
**Causa:** Dois componentes com o mesmo ID na mesma página  
**Solução:** Use o parâmetro `key` com valores diferentes:
```python
st.selectbox("Livro", opcoes, key="select1")  # Em uma tab
st.selectbox("Livro", opcoes, key="select2")  # Em outra tab
```

### Tabs não aparecem
**Causa:** Erro de sintaxe na criação das tabs  
**Solução:** Verifique se a linha das tabs está correta:
```python
tab1, tab2, tab3, tab4 = st.tabs([...])
```

### Conteúdo não aparece na tab
**Causa:** Indentação incorreta do código dentro do `with`  
**Solução:** Todo código da tab deve estar indentado após o `with`:
```python
with tab1:
    st.write("Correto")  # 4 espaços de indentação
```

## 📖 Componentes Novos Usados

| Componente | Para que serve | Exemplo |
|------------|----------------|---------|
| `st.tabs()` | Cria abas/guias | `tab1, tab2 = st.tabs(["A", "B"])` |
| `with` | Define contexto de uma tab | `with tab1: st.write("Oi")` |
| `st.info()` | Mensagem informativa azul | `st.info("Informação")` |
| `st.warning()` | Mensagem de aviso laranja | `st.warning("Cuidado!")` |
| `st.metric()` | Exibir métricas/números | `st.metric("Total", "10")` |
| `st.sidebar` | Barra lateral | `with st.sidebar: st.write("Lado")` |
| `key` | ID único para componentes | `st.text_input("Nome", key="nome1")` |

---

## 📚 Referências Úteis

- [Documentação Streamlit - Tabs](https://docs.streamlit.io/library/api-reference/layout/st.tabs)
- [Documentação Streamlit - Columns](https://docs.streamlit.io/library/api-reference/layout/st.columns)
- [Documentação Streamlit - Sidebar](https://docs.streamlit.io/library/api-reference/layout/st.sidebar)
- [Cheat Sheet Streamlit](https://cheat-sheet.streamlit.app/)

---

## 🎯 Resultado Esperado

Ao final desta atividade, você terá criado uma **interface visual completa** de um sistema CRUD, com 4 páginas organizadas em tabs. Na próxima atividade, você aprenderá a conectar essas páginas com um banco de dados SQLite para que as funcionalidades realmente funcionem!

---

**📝 Observação Importante:** Não se preocupe se clicar nos botões e nada acontecer (além da mensagem informativa). Isso é esperado! O foco desta atividade é a **estrutura e organização visual** das páginas. As funcionalidades virão depois! 🚀

---

**Boa sorte! 📚✨**

*Em caso de dúvidas, consulte o material do módulo ou procure o professor.*
