# Comparação: SQL Puro vs SQLAlchemy ORM

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

### SQLAlchemy ORM

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração
engine = create_engine('sqlite:///filmes.db', 
                      connect_args={"check_same_thread": False})
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# Definir modelo
class Filme(Base):
    __tablename__ = 'filmes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)

# Criar tabelas
Base.metadata.create_all(bind=engine)

# Obter sessão
session = SessionLocal()
```

**Vantagem SQLAlchemy:** Configuração mais verbosa inicialmente, mas muito mais poderosa e organizada.

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

### SQLAlchemy ORM

```python
def criar_filme(session, nome, ano, nota):
    try:
        filme = Filme(nome=nome, ano=ano, nota=nota)
        session.add(filme)
        session.commit()
        session.refresh(filme)  # Para obter o ID gerado
        return filme
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return None

# Usar
session = SessionLocal()
filme = criar_filme(session, "Inception", 2010, 9.5)
print(f"ID gerado: {filme.id}")  # Acesso direto ao ID
session.close()
```

**Vantagem SQLAlchemy:** 
- Retorna objeto com ID automaticamente
- Trabalhamos com objetos Python ao invés de tuplas
- Rollback automático em caso de erro

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

### SQLAlchemy ORM

```python
# Listar todos
def listar_filmes(session):
    filmes = session.query(Filme)\
        .order_by(Filme.ano.desc())\
        .all()
    return filmes

# Usar
session = SessionLocal()
filmes = listar_filmes(session)
for filme in filmes:
    print(f"{filme.id} - {filme.nome} ({filme.ano}) - {filme.nota}")
    # Atributos nomeados - muito mais legível!
session.close()
```

**Vantagem SQLAlchemy:** 
- Acesso a atributos por nome (filme.nome vs filme[1])
- Autocomplete do editor funciona
- Menos erros de índice

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

### SQLAlchemy ORM

```python
# Buscar por ID
def buscar_por_id(session, filme_id):
    return session.query(Filme)\
        .filter(Filme.id == filme_id)\
        .first()

# Buscar por nome (parcial)
def buscar_por_nome(session, nome):
    return session.query(Filme)\
        .filter(Filme.nome.ilike(f"%{nome}%"))\
        .all()

# Filtrar por ano
def filtrar_por_ano(session, ano_min, ano_max):
    return session.query(Filme)\
        .filter(Filme.ano >= ano_min)\
        .filter(Filme.ano <= ano_max)\
        .all()

# Ou com múltiplos filtros:
from sqlalchemy import and_

def filtrar_avancado(session, nome=None, ano_min=None, nota_min=None):
    query = session.query(Filme)
    
    if nome:
        query = query.filter(Filme.nome.ilike(f"%{nome}%"))
    if ano_min:
        query = query.filter(Filme.ano >= ano_min)
    if nota_min:
        query = query.filter(Filme.nota >= nota_min)
    
    return query.all()
```

**Vantagem SQLAlchemy:** 
- Queries podem ser construídas dinamicamente
- Métodos encadeáveis
- Proteção contra SQL injection automática
- Código mais legível

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

### SQLAlchemy ORM

```python
def atualizar_filme(session, filme_id, nome=None, ano=None, nota=None):
    try:
        filme = session.query(Filme)\
            .filter(Filme.id == filme_id)\
            .first()
        
        if not filme:
            return False
        
        # Atualizar apenas os campos fornecidos
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return False
```

**Vantagem SQLAlchemy:** 
- Trabalha diretamente com o objeto
- Não precisa reconstruir todo o registro
- Rollback automático
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

### SQLAlchemy ORM

```python
def deletar_filme(session, filme_id):
    try:
        filme = session.query(Filme)\
            .filter(Filme.id == filme_id)\
            .first()
        
        if not filme:
            return False
        
        session.delete(filme)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro: {e}")
        return False
```

**Vantagem SQLAlchemy:** 
- Mais seguro (verifica se existe antes)
- Rollback automático
- Pode executar lógica antes de deletar

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
def melhor_nota():
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

### SQLAlchemy ORM

```python
from sqlalchemy import func

# Contar filmes
def contar_filmes(session):
    return session.query(Filme).count()

# Média de notas
def media_notas(session):
    media = session.query(func.avg(Filme.nota)).scalar()
    return round(media, 2) if media else 0

# Melhor nota
def melhor_nota(session):
    return session.query(Filme)\
        .order_by(Filme.nota.desc())\
        .first()

# Filmes por ano
def filmes_por_ano(session):
    return session.query(
        Filme.ano, 
        func.count(Filme.id)
    ).group_by(Filme.ano)\
     .order_by(Filme.ano)\
     .all()
```

**Vantagem SQLAlchemy:** 
- Funções agregadas integradas
- Retorna objetos ou valores diretos
- Mais fácil de combinar com filtros

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

### SQLAlchemy ORM - Relacionamentos

```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Diretor(Base):
    __tablename__ = 'diretores'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    
    # Relacionamento
    filmes = relationship("Filme", back_populates="diretor")

class Filme(Base):
    __tablename__ = 'filmes'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    diretor_id = Column(Integer, ForeignKey('diretores.id'))
    
    # Relacionamento
    diretor = relationship("Diretor", back_populates="filmes")

# Usar - super simples!
filme = session.query(Filme).filter(Filme.id == 1).first()
print(f"Filme: {filme.nome}")
print(f"Diretor: {filme.diretor.nome}")  # Acesso direto!

# Ou o contrário
diretor = session.query(Diretor).filter(Diretor.id == 1).first()
for filme in diretor.filmes:  # Lista de filmes do diretor
    print(filme.nome)
```

**Vantagem SQLAlchemy:** 
- Relacionamentos definidos uma vez
- Navegação natural entre objetos
- Lazy/Eager loading configurável
- JOIN automático quando necessário

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

### SQLAlchemy ORM

✅ **Vantagens:**
- Código orientado a objetos
- Autocomplete do editor
- Proteção contra SQL injection
- Portável entre bancos de dados
- Relacionamentos simples
- Migrações facilitadas
- Código mais limpo e manutenível

❌ **Desvantagens:**
- Curva de aprendizado inicial
- Overhead de performance (pequeno)
- Queries complexas podem ser difíceis
- Mais dependências

---

## 🎯 Quando Usar Cada Um?

### Use SQL Puro quando:
- Projeto muito simples
- Performance crítica
- Query SQL complexa específica
- Aprendendo SQL

### Use SQLAlchemy quando:
- Projeto médio/grande
- Múltiplas tabelas relacionadas
- Precisa trocar de banco no futuro
- Trabalho em equipe
- Manutenção a longo prazo

---

## 💡 Conclusão

Para o ensino, é importante:

1. **Começar com SQL puro** (módulos 1-3) para entender os fundamentos
2. **Migrar para ORM** (módulo 4) para ver as vantagens
3. **Saber ambos** - o ideal é conhecer os dois e escolher conforme a necessidade

SQLAlchemy não substitui SQL - ele constrói sobre SQL. Entender SQL é fundamental mesmo usando ORM!

---

**A melhor ferramenta é aquela que você conhece bem e que resolve seu problema! 🚀**
