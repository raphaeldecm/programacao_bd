# Exercícios - Módulo 3: Aplicação Web com Streamlit

## 🎯 Exercícios Básicos

### Exercício 1: Filtro de Busca por Nome
**Objetivo:** Adicionar um campo de busca na aba "Listar Filmes" para filtrar filmes por nome.

**Instruções:**
1. Na aba "Listar Filmes", adicione um `st.text_input()` para busca
2. Filtre o DataFrame com base no texto digitado
3. Exiba apenas os filmes que contêm o texto no nome (case-insensitive)

**Dica:**
```python
busca = st.text_input("🔍 Buscar filme por nome")
if busca:
    df = df[df['Nome'].str.contains(busca, case=False)]
```

---

### Exercício 2: Ordenação da Lista
**Objetivo:** Permitir que o usuário escolha como ordenar a lista de filmes.

**Instruções:**
1. Adicione um `st.selectbox()` com opções: "Nome", "Ano", "Nota"
2. Adicione também a opção de ordenação crescente/decrescente
3. Ordene o DataFrame conforme a seleção do usuário

**Dica:**
```python
ordem_por = st.selectbox("Ordenar por:", ["Nome", "Ano", "Nota"])
crescente = st.checkbox("Ordem crescente", value=True)
df = df.sort_values(by=ordem_por, ascending=crescente)
```

---

### Exercício 3: Estatísticas Expandidas
**Objetivo:** Adicionar mais estatísticas na visualização dos filmes.

**Instruções:**
1. Adicione métricas para: "Pior Nota", "Filme Mais Antigo", "Filme Mais Recente"
2. Use `st.metric()` para exibir as informações
3. Organize em uma grade com `st.columns()`

---

### Exercício 4: Validação de Filmes Duplicados
**Objetivo:** Impedir a adição de filmes com mesmo nome e ano.

**Instruções:**
1. Antes de adicionar um filme, verifique se já existe um com mesmo nome e ano
2. Se existir, exiba uma mensagem de erro com `st.error()`
3. Não permita a adição do filme duplicado

**Dica:**
```python
# Verificar duplicatas
filmes_existentes = db.listar_filmes()
for filme in filmes_existentes:
    if filme[1].lower() == nome.lower() and filme[2] == ano:
        st.error("Filme já cadastrado!")
        return
```

---

### Exercício 5: Exportação em CSV
**Objetivo:** Permitir que o usuário baixe a lista de filmes em formato CSV.

**Instruções:**
1. Na aba "Listar Filmes", adicione um botão de download
2. Use `st.download_button()` para permitir o download
3. O arquivo deve conter todos os filmes no formato CSV

**Dica:**
```python
csv = df.to_csv(index=False)
st.download_button(
    label="📥 Download CSV",
    data=csv,
    file_name="filmes.csv",
    mime="text/csv"
)
```

---

## 🚀 Exercícios Intermediários

### Exercício 6: Gráfico de Filmes por Ano
**Objetivo:** Criar um gráfico de barras mostrando quantos filmes existem por ano.

**Instruções:**
1. Agrupe os filmes por ano
2. Use `st.bar_chart()` ou `st.plotly_chart()` para exibir
3. Adicione em uma nova seção na aba de listagem

**Dica:**
```python
filmes_por_ano = df.groupby('Ano').size()
st.bar_chart(filmes_por_ano)
```

---

### Exercício 7: Filtros Múltiplos
**Objetivo:** Adicionar filtros por ano e nota mínima.

**Instruções:**
1. Crie um filtro com `st.slider()` para intervalo de anos
2. Crie outro filtro para nota mínima
3. Aplique os filtros simultaneamente ao DataFrame

**Exemplo:**
```python
col1, col2 = st.columns(2)
with col1:
    ano_min, ano_max = st.slider("Período", 1900, 2030, (2000, 2024))
with col2:
    nota_min = st.slider("Nota mínima", 0.0, 10.0, 0.0)

df_filtrado = df[
    (df['Ano'] >= ano_min) & 
    (df['Ano'] <= ano_max) & 
    (df['Nota'] >= nota_min)
]
```

---

### Exercício 8: Sidebar com Informações
**Objetivo:** Criar uma barra lateral com estatísticas e opções.

**Instruções:**
1. Use `st.sidebar` para criar uma barra lateral
2. Exiba estatísticas gerais (total de filmes, média, etc.)
3. Adicione opções de configuração (tema, limite de exibição, etc.)

**Dica:**
```python
with st.sidebar:
    st.header("📊 Estatísticas Gerais")
    total = len(db.listar_filmes())
    st.metric("Total de Filmes", total)
```

---

### Exercício 9: Confirmação Antes de Deletar
**Objetivo:** Melhorar a experiência de exclusão com confirmação dupla.

**Instruções:**
1. Use `st.checkbox()` para confirmar a intenção de deletar
2. Só habilite o botão de exclusão se o checkbox estiver marcado
3. Adicione uma mensagem clara sobre a ação irreversível

**Exemplo:**
```python
confirmar = st.checkbox("Eu confirmo que quero deletar este filme")
if st.button("Deletar", disabled=not confirmar):
    # deletar
```

---

### Exercício 10: Edição em Lote
**Objetivo:** Permitir atualizar a nota de vários filmes de uma vez.

**Instruções:**
1. Crie uma nova aba "Edição em Lote"
2. Use `st.multiselect()` para selecionar múltiplos filmes
3. Permita definir uma nova nota para todos os selecionados
4. Atualize todos de uma vez

---

## 🏆 Exercícios Avançados

### Exercício 11: Paginação da Lista
**Objetivo:** Implementar paginação para listas grandes de filmes.

**Instruções:**
1. Defina um número máximo de filmes por página (ex: 10)
2. Use `st.number_input()` ou botões para navegar entre páginas
3. Exiba apenas os filmes da página atual

**Dica:**
```python
filmes_por_pagina = 10
pagina = st.number_input("Página", min_value=1, max_value=total_paginas)
inicio = (pagina - 1) * filmes_por_pagina
fim = inicio + filmes_por_pagina
df_pagina = df[inicio:fim]
```

---

### Exercício 12: Importação de CSV
**Objetivo:** Permitir importar filmes de um arquivo CSV.

**Instruções:**
1. Crie uma nova aba "Importar Dados"
2. Use `st.file_uploader()` para upload de CSV
3. Valide os dados e insira no banco
4. Exiba um resumo da importação

**Dica:**
```python
arquivo = st.file_uploader("Escolha um arquivo CSV", type=['csv'])
if arquivo:
    df = pd.read_csv(arquivo)
    st.dataframe(df)
```

---

### Exercício 13: Gráfico de Distribuição de Notas
**Objetivo:** Criar um histograma mostrando a distribuição das notas.

**Instruções:**
1. Use `st.plotly_chart()` ou `matplotlib`
2. Crie um histograma das notas
3. Mostre quantos filmes existem em cada faixa de nota (0-2, 2-4, etc.)

---

### Exercício 14: Sistema de Favoritos
**Objetivo:** Adicionar um campo "favorito" aos filmes.

**Instruções:**
1. Modifique a tabela do banco para incluir um campo `favorito` (boolean)
2. Adicione um checkbox na hora de adicionar/editar filmes
3. Crie um filtro para mostrar apenas favoritos
4. Use ⭐ para indicar favoritos na listagem

**Dica - Alterar tabela:**
```python
def adicionar_coluna_favorito():
    try:
        self.cursor.execute(
            "ALTER TABLE filmes ADD COLUMN favorito INTEGER DEFAULT 0"
        )
        self.connection.commit()
    except sqlite3.Error:
        pass  # Coluna já existe
```

---

### Exercício 15: Temas Personalizados
**Objetivo:** Criar opções de personalização da interface.

**Instruções:**
1. Crie um arquivo `.streamlit/config.toml`
2. Configure cores personalizadas
3. Adicione opções na sidebar para alternar entre temas (opcional - avançado)

**Exemplo de config.toml:**
```toml
[theme]
primaryColor = "#FF4B4B"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

---

## 🎓 Projeto Final: Sistema Completo de Biblioteca

**Objetivo:** Criar um sistema completo de gerenciamento de biblioteca com múltiplas tabelas.

**Requisitos:**
1. Tabela de **Livros** (título, autor, ano, ISBN, disponível)
2. Tabela de **Usuários** (nome, email, telefone)
3. Tabela de **Empréstimos** (livro, usuário, data empréstimo, data devolução)
4. Interface para gerenciar todas as operações
5. Relatórios (livros mais emprestados, usuários ativos, etc.)
6. Sistema de busca avançada
7. Exportação de relatórios em PDF ou CSV

**Funcionalidades Extras:**
- Notificação de atraso na devolução
- Reserva de livros
- Histórico de empréstimos
- Dashboard com gráficos estatísticos

---

## 💡 Dicas para os Exercícios

1. **Teste cada funcionalidade** antes de passar para a próxima
2. **Leia a documentação** do Streamlit quando tiver dúvidas
3. **Use st.write() ou st.json()** para debugar variáveis
4. **Crie funções auxiliares** para manter o código organizado
5. **Comente seu código** para facilitar o entendimento
6. **Use Git** para versionar seu progresso

---

## 📚 Recursos de Apoio

- [Documentação Streamlit](https://docs.streamlit.io/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Streamlit Gallery - Exemplos](https://streamlit.io/gallery)

---

**Bons estudos e divirta-se programando! 🚀**
