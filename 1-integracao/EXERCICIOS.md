# Lista de Exercícios - Módulo 1

## Exercícios Práticos de Python + SQLite

### Exercício 1: Loja de Sapatos
Crie um banco de dados para uma loja de sapatos e realize as quatro operações CRUD.

**Estrutura da tabela:**
```sql
CREATE TABLE sapatos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT NOT NULL,
    modelo TEXT NOT NULL,
    tamanho INTEGER NOT NULL,
    preco REAL NOT NULL,
    cor TEXT NOT NULL
);
```

**Tarefas:**
1. Conecte ao banco `loja_sapatos.db`
2. Crie a tabela `sapatos`
3. Insira 5 sapatos diferentes
4. Liste todos os sapatos
5. Atualize o preço de um sapato
6. Delete um sapato

---

### Exercício 2: Biblioteca Escolar
Crie um sistema para controlar livros de uma biblioteca.

**Estrutura da tabela:**
```sql
CREATE TABLE livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    disponivel BOOLEAN DEFAULT 1
);
```

**Tarefas:**
1. Conecte ao banco `biblioteca.db`
2. Crie a tabela `livros`
3. Insira 3 livros
4. Liste apenas livros disponíveis
5. Marque um livro como emprestado (disponivel = 0)
6. Delete um livro específico

---

### Exercício 3: Controle de Estoque
Sistema simples para controlar produtos em estoque.

**Estrutura da tabela:**
```sql
CREATE TABLE produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    categoria TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    preco REAL NOT NULL
);
```

**Tarefas:**
1. Conecte ao banco `estoque.db`
2. Crie a tabela `produtos`
3. Insira 4 produtos de categorias diferentes
4. Liste produtos com quantidade menor que 10
5. Aumente a quantidade de um produto em 5 unidades
6. Remove produtos com quantidade zero

---

### Exercício 4: Cadastro de Alunos
Sistema para cadastrar alunos de uma turma.

**Estrutura da tabela:**
```sql
CREATE TABLE alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL,
    turma TEXT NOT NULL,
    nota REAL
);
```

**Tarefas:**
1. Conecte ao banco `escola.db`
2. Crie a tabela `alunos`
3. Insira 6 alunos de turmas diferentes
4. Liste alunos de uma turma específica
5. Atualize a nota de um aluno
6. Delete alunos sem nota (nota = NULL)

---

### Exercício 5: Cardápio de Restaurante
Sistema para gerenciar pratos de um restaurante.

**Estrutura da tabela:**
```sql
CREATE TABLE pratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    preco REAL NOT NULL,
    ingredientes TEXT
);
```

**Tarefas:**
1. Conecte ao banco `restaurante.db`
2. Crie a tabela `pratos`
3. Insira 5 pratos (entrada, prato principal, sobremesa)
4. Liste pratos por tipo
5. Atualize o preço de todos os pratos em 10%
6. Delete pratos mais caros que R$ 50,00

---

## Instruções Gerais

### Para cada exercício:
1. Crie um arquivo Python separado
2. Use consultas parametrizadas (com `?`)
3. Trate erros com try/except
4. Teste seu código

### Exemplo de estrutura:
```python
import sqlite3

try:
    # 1. Conectar
    conn = sqlite3.connect('nome_banco.db')
    cursor = conn.cursor()
    
    # 2. Criar tabela
    cursor.execute("CREATE TABLE...")
    
    # 3. Inserir dados
    cursor.execute("INSERT INTO...")
    
    # 4. Consultar
    cursor.execute("SELECT...")
    
    # 5. Atualizar
    cursor.execute("UPDATE...")
    
    # 6. Deletar
    cursor.execute("DELETE...")
    
    conn.commit()
    print("Operações realizadas com sucesso!")
    
except sqlite3.Error as e:
    print(f"Erro: {e}")
    
finally:
    conn.close()
```

### Entrega:
- Arquivo .py para cada exercício
- Código funcionando sem erros
- Comentários explicando cada operação