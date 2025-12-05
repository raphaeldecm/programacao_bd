# Comparação: SQL Puro vs Peewee ORM

## 📊 Visão Geral

Este documento compara as duas abordagens para trabalhar com bancos de dados em Python, mostrando exemplos práticos lado a lado.

---

## 🔧 Configuração e Conexão

### SQL Puro (sqlite3)

```python
import sqlite3

# Criar conexão
connection = sqlite3.connect('filmes.db', check_same_thread=False)
cursor = connection.cursor()

# Criar tabela
cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
    )
""")
connection.commit()
```

### Peewee ORM

```python
from peewee import SqliteDatabase, Model, AutoField, CharField, IntegerField, FloatField

# Configuração
db = SqliteDatabase('filmes.db')

# Definir modelo
class Filme(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    ano = IntegerField(null=False)
    nota = FloatField(null=False)
    
    class Meta:
        database = db
        table_name = 'filmes'

# Criar tabelas
db.connect()
db.create_tables([Filme], safe=True)
```

**Vantagem Peewee:** Definição declarativa mais limpa e orientada a objetos.

---

## ➕ CREATE - Inserir Dados

### SQL Puro

```python
def criar_filme(nome, ano, nota):
    try:
        cursor.execute("""
            INSERT INTO filmes (nome, ano, nota) 
            VALUES (?, ?, ?)
        """, (nome, ano, nota))
        connection.commit()
        return True
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False

# Usar
criar_filme("Inception", 2010, 9.5)
```

### Peewee ORM

```python
def criar_filme(nome, ano, nota):
    try:
        filme = Filme.create(nome=nome, ano=ano, nota=nota)
        return filme
    except Exception as e:
        print(f"Erro: {e}")
        return None

# Usar
filme = criar_filme("Inception", 2010, 9.5)
print(f"ID gerado: {filme.id}")  # Acesso direto ao ID
```

**Vantagem Peewee:**
- Uma linha de código ao invés de três (create, commit)
- Retorna objeto completo com ID
- Mais intuitivo e Pythônico

---

## 📖 READ - Buscar Dados

### SQL Puro

```python
# Listar todos
def listar_filmes():
    cursor.execute("""
        SELECT id, nome, ano, nota 
        FROM filmes 
        ORDER BY ano DESC
    """)
    return cursor.fetchall()

# Usar
filmes = listar_filmes()
for filme in filmes:
    print(f"{filme[0]} - {filme[1]} ({filme[2]}) - {filme[3]}")
    # Índices numéricos - difícil de ler!
```

### Peewee ORM

```python
# Listar todos
def listar_filmes():
    filmes = Filme.select().order_by(Filme.ano.desc())
    return list(filmes)

# Usar
filmes = listar_filmes()
for filme in filmes:
    print(f"{filme.id} - {filme.nome} ({filme.ano}) - {filme.nota}")
    # Atributos nomeados - muito mais legível!
```

**Vantagem Peewee:**
- Acesso a atributos por nome (filme.nome vs filme[1])
- Autocomplete do editor funciona
- Menos erros de índice
- Código auto-documentado

---

## 🔍 Buscas e Filtros

### SQL Puro

```python
# Buscar por ID
def buscar_por_id(filme_id):
    cursor.execute("""
        SELECT id, nome, ano, nota 
        FROM filmes 
        WHERE id = ?
    """, (filme_id,))
    return cursor.fetchone()

# Buscar por nome (parcial)
def buscar_por_nome(nome):
    cursor.execute("""
        SELECT id, nome, ano, nota 
        FROM filmes 
        WHERE nome LIKE ?
    """, (f"%{nome}%",))
    return cursor.fetchall()

# Filtrar por ano
def filtrar_por_ano(ano_min, ano_max):
    cursor.execute("""
        SELECT id, nome, ano, nota 
        FROM filmes 
        WHERE ano >= ? AND ano <= ?
    """, (ano_min, ano_max))
    return cursor.fetchall()
```

### Peewee ORM

```python
from peewee import DoesNotExist

# Buscar por ID
def buscar_por_id(filme_id):
    try:
        return Filme.get_by_id(filme_id)
    except DoesNotExist:
        return None

# Buscar por nome (parcial)
def buscar_por_nome(nome):
    return list(Filme.select().where(
        Filme.nome.contains(nome)
    ))

# Filtrar por ano
def filtrar_por_ano(ano_min, ano_max):
    return list(Filme.select().where(
        (Filme.ano >= ano_min) & (Filme.ano <= ano_max)
    ))

# Filtros dinâmicos
def buscar_avancado(nome=None, ano_min=None, nota_min=None):
    query = Filme.select()
    
    if nome:
        query = query.where(Filme.nome.contains(nome))
    if ano_min:
        query = query.where(Filme.ano >= ano_min)
    if nota_min:
        query = query.where(Filme.nota >= nota_min)
    
    return list(query)
```

**Vantagem Peewee:**
- Queries construídas dinamicamente
- Métodos encadeáveis (.where().order_by().limit())
- Proteção contra SQL injection automática
- Exceção específica (DoesNotExist) para busca por ID

---

## ✏️ UPDATE - Atualizar Dados

### SQL Puro

```python
def atualizar_filme(filme_id, nome=None, ano=None, nota=None):
    # Buscar filme atual
    filme = buscar_por_id(filme_id)
    if not filme:
        return False
    
    # Manter valores antigos se não fornecidos
    novo_nome = nome if nome is not None else filme[1]
    novo_ano = ano if ano is not None else filme[2]
    nova_nota = nota if nota is not None else filme[3]
    
    try:
        cursor.execute("""
            UPDATE filmes 
            SET nome = ?, ano = ?, nota = ? 
            WHERE id = ?
        """, (novo_nome, novo_ano, nova_nota, filme_id))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False
```

### Peewee ORM

```python
def atualizar_filme(filme_id, nome=None, ano=None, nota=None):
    try:
        filme = Filme.get_by_id(filme_id)
        
        # Atualizar apenas os campos fornecidos
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        
        filme.save()  # Salva apenas campos modificados!
        return True
    except DoesNotExist:
        return False
    except Exception as e:
        print(f"Erro: {e}")
        return False
```

**Vantagem Peewee:**
- Trabalha diretamente com o objeto
- `.save()` atualiza apenas campos modificados (eficiente!)
- Não precisa reconstruir todo o registro
- Mais intuitivo

---

## 🗑️ DELETE - Deletar Dados

### SQL Puro

```python
def deletar_filme(filme_id):
    try:
        cursor.execute("""
            DELETE FROM filmes 
            WHERE id = ?
        """, (filme_id,))
        connection.commit()
        return cursor.rowcount > 0
    except sqlite3.Error as e:
        print(f"Erro: {e}")
        return False
```

### Peewee ORM

```python
def deletar_filme(filme_id):
    try:
        filme = Filme.get_by_id(filme_id)
        filme.delete_instance()
        return True
    except DoesNotExist:
        return False
    except Exception as e:
        print(f"Erro: {e}")
        return False
```

**Vantagem Peewee:**
- Mais seguro (verifica se existe antes)
- Pode executar lógica antes de deletar
- Código mais expressivo

---

## 📊 Agregações e Estatísticas

### SQL Puro

```python
# Contar filmes
def contar_filmes():
    cursor.execute("SELECT COUNT(*) FROM filmes")
    return cursor.fetchone()[0]

# Média de notas
def media_notas():
    cursor.execute("SELECT AVG(nota) FROM filmes")
    resultado = cursor.fetchone()[0]
    return round(resultado, 2) if resultado else 0

# Melhor nota
def melhor_filme():
    cursor.execute("""
        SELECT nome, nota 
        FROM filmes 
        ORDER BY nota DESC 
        LIMIT 1
    """)
    return cursor.fetchone()

# Filmes por ano
def filmes_por_ano():
    cursor.execute("""
        SELECT ano, COUNT(*) 
        FROM filmes 
        GROUP BY ano 
        ORDER BY ano
    """)
    return cursor.fetchall()
```

### Peewee ORM

```python
from peewee import fn

# Contar filmes
def contar_filmes():
    return Filme.select().count()

# Média de notas
def media_notas():
    media = Filme.select(fn.AVG(Filme.nota)).scalar()
    return round(media, 2) if media else 0

# Melhor filme
def melhor_filme():
    return (Filme.select()
            .order_by(Filme.nota.desc())
            .first())

# Filmes por ano
def filmes_por_ano():
    return list(
        Filme.select(Filme.ano, fn.COUNT(Filme.id).alias('total'))
        .group_by(Filme.ano)
        .order_by(Filme.ano)
    )
```

**Vantagem Peewee:**
- Funções agregadas integradas (fn.AVG, fn.COUNT, etc.)
- Retorna objetos ou valores diretos
- Mais fácil de combinar com filtros
- Queries complexas mais legíveis

---

## 🔗 Relacionamentos (Exemplo Avançado)

### SQL Puro - Tabelas Relacionadas

```python
# Criar tabelas
cursor.execute("""
    CREATE TABLE diretores (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE filmes (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        diretor_id INTEGER,
        FOREIGN KEY (diretor_id) REFERENCES diretores(id)
    )
""")

# Buscar filme com diretor (JOIN)
def buscar_filme_com_diretor(filme_id):
    cursor.execute("""
        SELECT f.id, f.nome, d.nome
        FROM filmes f
        LEFT JOIN diretores d ON f.diretor_id = d.id
        WHERE f.id = ?
    """, (filme_id,))
    return cursor.fetchone()
```

### Peewee ORM - Relacionamentos

```python
from peewee import ForeignKeyField

class Diretor(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    
    class Meta:
        database = db
        table_name = 'diretores'

class Filme(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    diretor = ForeignKeyField(Diretor, backref='filmes')
    
    class Meta:
        database = db
        table_name = 'filmes'

# Usar - super simples!
filme = Filme.get_by_id(1)
print(f"Filme: {filme.nome}")
print(f"Diretor: {filme.diretor.nome}")  # Acesso direto!

# Ou o contrário
diretor = Diretor.get_by_id(1)
for filme in diretor.filmes:  # Lista de filmes do diretor
    print(filme.nome)
```

**Vantagem Peewee:**
- Relacionamentos definidos uma vez
- Navegação natural entre objetos
- JOIN automático quando necessário
- backref cria relação inversa automaticamente

---

## 📈 Resumo de Vantagens

### SQL Puro (sqlite3)

✅ **Vantagens:**
- Simples para começar
- Controle total sobre SQL
- Menos overhead
- Ideal para queries muito específicas

❌ **Desvantagens:**
- Strings SQL podem ter erros
- Índices numéricos confusos
- Difícil manter com muitas tabelas
- Propenso a SQL injection se mal usado
- Código repetitivo
- Precisa gerenciar commit/rollback manualmente

### Peewee ORM

✅ **Vantagens:**
- Código orientado a objetos
- Autocomplete do editor
- Proteção contra SQL injection
- Portável entre bancos de dados
- Relacionamentos simples
- Código mais limpo e manutenível
- Menos linhas de código
- Similar ao Django ORM
- Não precisa gerenciar sessões

❌ **Desvantagens:**
- Curva de aprendizado inicial
- Overhead de performance (pequeno)
- Queries muito complexas podem ser difíceis
- Mais dependências

---

## 🎯 Quando Usar Cada Um?

### Use SQL Puro quando

- Projeto muito simples (script único)
- Performance extremamente crítica
- Query SQL complexa muito específica
- Aprendendo SQL puro

### Use Peewee quando

- Projeto médio/grande
- Múltiplas tabelas relacionadas
- Precisa trocar de banco no futuro
- Trabalho em equipe
- Manutenção a longo prazo
- Preparação para Django

---

## 💡 Conclusão

Para o ensino, é importante:

1. **Começar com SQL puro** (módulos 1-3) para entender os fundamentos
2. **Migrar para ORM** (módulo 4) para ver as vantagens
3. **Saber ambos** - o ideal é conhecer os dois e escolher conforme a necessidade

Peewee não substitui SQL - ele constrói sobre SQL. Entender SQL é fundamental mesmo usando ORM!

---

**A melhor ferramenta é aquela que você conhece bem e que resolve seu problema! 🚀**
