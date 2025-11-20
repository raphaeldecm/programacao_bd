# Exercícios - Módulo 3: Aplicação Web com Streamlit

## 🎯 Exercícios Básicos

### Exercício 1: Filtro de Busca por Nome
**Objetivo:** Adicionar um campo de busca na aba "Listar Filmes" para filtrar filmes por nome.

**Instruções:**
1. Na aba "Listar Filmes", adicione um `st.text_input()` para busca
2. Filtre a lista de filmes com base no texto digitado
3. Exiba apenas os filmes que contêm o texto no nome (case-insensitive)

**Dica:**
```python
busca = st.text_input("🔍 Buscar filme por nome")
if busca:
    filmes = [f for f in filmes if busca.lower() in f[1].lower()]
```

---

### Exercício 2: Contador de Filmes por Década
**Objetivo:** Mostrar quantos filmes existem em cada década.

**Instruções:**
1. Na aba "Listar Filmes", após mostrar todos os filmes
2. Conte quantos filmes existem para cada década (1990s, 2000s, 2010s, etc.)
3. Exiba o resultado de forma clara

**Dica:**
```python
# Agrupar por década
decadas = {}
for filme in filmes:
    decada = (filme[2] // 10) * 10  # Ex: 2023 -> 2020
    decadas[decada] = decadas.get(decada, 0) + 1
```

---

### Exercício 3: Validação de Filmes Duplicados
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
        # não adicionar
```

---

### Exercício 4: Mensagem quando não há filmes
**Objetivo:** Melhorar a experiência quando não existem filmes cadastrados.

**Instruções:**
1. Nas abas "Atualizar" e "Deletar", se não houver filmes
2. Adicione uma mensagem amigável usando `st.info()` ou `st.warning()`
3. Sugira que o usuário adicione filmes na primeira aba

---

### Exercício 5: Botão de Recarregar Lista
**Objetivo:** Adicionar um botão para atualizar a lista de filmes manualmente.

**Instruções:**
1. Na aba "Listar Filmes", adicione um botão "Recarregar"
2. Use `st.button()` e `st.rerun()` para recarregar a página
3. Isso é útil para ver alterações feitas em outras abas

---

## 🚀 Exercícios Intermediários

### Exercício 6: Estatísticas Básicas
**Objetivo:** Mostrar informações estatísticas sobre os filmes cadastrados.

**Instruções:**
1. Na aba "Listar Filmes", calcule e exiba:
   - Nota média dos filmes
   - Filme com melhor nota
   - Filme com pior nota
2. Use `st.metric()` ou simplesmente `st.write()`

**Dica:**
```python
notas = [filme[3] for filme in filmes]
media = sum(notas) / len(notas)
st.write(f"📊 Nota média: {media:.2f}")
```

---

### Exercício 7: Ordenação da Lista
**Objetivo:** Permitir ordenar os filmes por diferentes critérios.

**Instruções:**
1. Adicione um `st.selectbox()` para escolher ordenação (Nome, Ano, Nota)
2. Adicione um `st.checkbox()` para ordem crescente/decrescente
3. Ordene a lista conforme selecionado

**Dica:**
```python
ordem = st.selectbox("Ordenar por:", ["Nome", "Ano", "Nota"])
# Índices: 0=ID, 1=Nome, 2=Ano, 3=Nota
indice = {"Nome": 1, "Ano": 2, "Nota": 3}[ordem]
filmes_ordenados = sorted(filmes, key=lambda x: x[indice])
```

---

### Exercício 8: Barra de Progresso na Nota
**Objetivo:** Visualizar a nota como uma barra de progresso.

**Instruções:**
1. Na listagem de filmes, ao invés de mostrar só o número
2. Use `st.progress()` para mostrar a nota visualmente
3. A barra deve ir de 0 a 10

**Dica:**
```python
st.progress(filme[3] / 10)  # Converte nota 0-10 para 0-1
```

---

### Exercício 9: Confirmação com Checkbox
**Objetivo:** Adicionar confirmação antes de deletar.

**Instruções:**
1. Na aba "Deletar", após selecionar o filme
2. Adicione um `st.checkbox()` "Confirmo que quero deletar"
3. Só permita deletar se o checkbox estiver marcado

**Dica:**
```python
confirmar = st.checkbox("Confirmo que quero deletar este filme")
if st.button("Deletar", disabled=not confirmar):
    # deletar
```

---

### Exercício 10: Campo de Gênero
**Objetivo:** Adicionar um novo campo "gênero" aos filmes.

**Instruções:**
1. Modifique a tabela do banco para incluir campo "genero"
2. Adicione um `st.selectbox()` na hora de adicionar filme
3. Opções: Ação, Comédia, Drama, Ficção, Terror, Romance
4. Exiba o gênero na listagem

---

## 🏆 Exercícios Avançados

### Exercício 11: Exportação para CSV
**Objetivo:** Permitir baixar a lista de filmes em formato CSV.

**Instruções:**
1. Na aba "Listar Filmes", crie o conteúdo CSV manualmente
2. Use `st.download_button()` para permitir o download
3. O arquivo deve ter: ID, Nome, Ano, Nota

**Dica:**
```python
# Criar CSV manualmente
csv = "ID,Nome,Ano,Nota\n"
for filme in filmes:
    csv += f"{filme[0]},{filme[1]},{filme[2]},{filme[3]}\n"

st.download_button("Download CSV", csv, "filmes.csv", "text/csv")
```

---

### Exercício 12: Filtro por Intervalo de Anos
**Objetivo:** Adicionar filtro para selecionar período de anos.

**Instruções:**
1. Use `st.slider()` com dois valores (range)
2. Filtre filmes entre o ano mínimo e máximo selecionado
3. Exiba apenas filmes nesse intervalo

**Dica:**
```python
ano_min, ano_max = st.slider("Período", 1900, 2030, (2000, 2024))
filmes_filtrados = [f for f in filmes if ano_min <= f[2] <= ano_max]
```

---

### Exercício 13: Sidebar com Estatísticas
**Objetivo:** Criar uma barra lateral com informações gerais.

**Instruções:**
1. Use `st.sidebar` para criar menu lateral
2. Mostre estatísticas (total de filmes, média de notas, etc.)
3. Adicione informações sobre o sistema

**Dica:**
```python
with st.sidebar:
    st.header("📊 Estatísticas")
    st.metric("Total de Filmes", len(filmes))
```

---

### Exercício 14: Sistema de Categorias
**Objetivo:** Adicionar categorias aos filmes (Ação, Comédia, Drama, etc.).

**Instruções:**
1. Altere a tabela do banco para incluir campo "categoria"
2. Na hora de adicionar, use `st.selectbox()` para escolher categoria
3. Permita filtrar filmes por categoria
4. Mostre quantos filmes há em cada categoria

**Dica - Alterar models.py:**
```python
# Adicionar na criação da tabela
categoria TEXT
```

---

### Exercício 15: Busca Avançada
**Objetivo:** Criar sistema de busca com múltiplos critérios.

**Instruções:**
1. Crie uma nova aba "Busca Avançada"
2. Permita buscar por: nome (parcial), intervalo de anos, nota mínima
3. Combine todos os filtros
4. Mostre quantos resultados foram encontrados

**Dica:**
```python
# Aplicar múltiplos filtros
resultados = filmes
if nome_busca:
    resultados = [f for f in resultados if nome_busca.lower() in f[1].lower()]
if nota_min:
    resultados = [f for f in resultados if f[3] >= nota_min]
```

---

## 🎓 Projeto Final: Sistema de Biblioteca Simples

**Objetivo:** Criar um sistema de gerenciamento de biblioteca focado em operações de banco de dados.

**Requisitos Mínimos:**
1. Tabela de **Livros** (id, título, autor, ano, disponível)
2. Operações CRUD completas para livros
3. Marcar livro como emprestado/disponível
4. Listar apenas livros disponíveis
5. Buscar livros por autor

**Requisitos Intermediários:**
6. Adicionar campo "categoria" (Ficção, Técnico, Romance, etc.)
7. Filtrar por categoria
8. Mostrar estatísticas (total de livros, quantos disponíveis, etc.)
9. Exportar lista em CSV

**Requisitos Avançados (Desafio):**
10. Segunda tabela de **Empréstimos** (id_livro, nome_pessoa, data_emprestimo)
11. Ao emprestar, marcar livro como indisponível
12. Ao devolver, marcar como disponível novamente
13. Mostrar histórico de empréstimos de um livro

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
