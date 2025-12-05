# Migração: SQLAlchemy → Peewee ORM

## 📋 Resumo da Migração

O módulo 4 foi atualizado de **SQLAlchemy** para **Peewee ORM** devido à:

- ✅ Maior simplicidade e menos boilerplate
- ✅ Sintaxe similar ao Django ORM (preparação para futuro)
- ✅ Não requer gerenciamento manual de sessões
- ✅ Código mais limpo e direto
- ✅ Melhor para ensino de iniciantes

---

## 🔄 Principais Mudanças

### 1. Configuração do Banco (`database.py`)

**Antes (SQLAlchemy):**
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///filmes.db')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def init_db():
    Base.metadata.create_all(bind=engine)
```

**Depois (Peewee):**
```python
from peewee import SqliteDatabase

db = SqliteDatabase('filmes.db', pragmas={'journal_mode': 'wal'})

def init_db():
    from models import Filme
    db.connect()
    db.create_tables([Filme], safe=True)

def close_db():
    if not db.is_closed():
        db.close()
```

**Vantagens:**
- ❌ Sem necessidade de SessionLocal
- ❌ Sem necessidade de get_session()
- ✅ Conexão global simplificada

---

### 2. Definição de Modelos (`models.py`)

**Antes (SQLAlchemy):**
```python
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Filme(Base):
    __tablename__ = 'filmes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
```

**Depois (Peewee):**
```python
from peewee import Model, AutoField, CharField, IntegerField, FloatField
from database import db

class Filme(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    ano = IntegerField(null=False)
    nota = FloatField(null=False)
    
    class Meta:
        database = db
        table_name = 'filmes'
```

**Vantagens:**
- ✅ Sintaxe mais limpa
- ✅ class Meta ao invés de __tablename__
- ✅ null= ao invés de nullable=

---

### 3. Operações CRUD (`crud.py`)

#### CREATE

**Antes (SQLAlchemy):**
```python
def criar_filme(session, nome, ano, nota):
    filme = Filme(nome=nome, ano=ano, nota=nota)
    session.add(filme)
    session.commit()
    session.refresh(filme)
    return filme
```

**Depois (Peewee):**
```python
def criar_filme(nome, ano, nota):
    filme = Filme.create(nome=nome, ano=ano, nota=nota)
    return filme
```

**Mudanças:**
- ❌ Sem parâmetro session
- ❌ Sem session.add()
- ❌ Sem session.commit()
- ❌ Sem session.refresh()
- ✅ Uma linha: Filme.create()

---

#### READ

**Antes (SQLAlchemy):**
```python
def listar_filmes(session):
    filmes = session.query(Filme).order_by(Filme.ano.desc()).all()
    return filmes

def buscar_filme_por_id(session, filme_id):
    filme = session.query(Filme).filter(Filme.id == filme_id).first()
    return filme
```

**Depois (Peewee):**
```python
def listar_filmes():
    filmes = Filme.select().order_by(Filme.ano.desc())
    return list(filmes)

def buscar_filme_por_id(filme_id):
    try:
        return Filme.get_by_id(filme_id)
    except DoesNotExist:
        return None
```

**Mudanças:**
- ❌ Sem session
- ✅ .select() ao invés de session.query()
- ✅ .get_by_id() método específico
- ✅ DoesNotExist exception mais específica

---

#### UPDATE

**Antes (SQLAlchemy):**
```python
def atualizar_filme(session, filme_id, nome=None, ano=None, nota=None):
    filme = buscar_filme_por_id(session, filme_id)
    if nome is not None:
        filme.nome = nome
    if ano is not None:
        filme.ano = ano
    if nota is not None:
        filme.nota = nota
    session.commit()
    return True
```

**Depois (Peewee):**
```python
def atualizar_filme(filme_id, nome=None, ano=None, nota=None):
    filme = buscar_filme_por_id(filme_id)
    if nome is not None:
        filme.nome = nome
    if ano is not None:
        filme.ano = ano
    if nota is not None:
        filme.nota = nota
    filme.save()
    return True
```

**Mudanças:**
- ❌ Sem session
- ✅ .save() ao invés de session.commit()
- ✅ save() atualiza apenas campos modificados

---

#### DELETE

**Antes (SQLAlchemy):**
```python
def deletar_filme(session, filme_id):
    filme = buscar_filme_por_id(session, filme_id)
    session.delete(filme)
    session.commit()
    return True
```

**Depois (Peewee):**
```python
def deletar_filme(filme_id):
    filme = buscar_filme_por_id(filme_id)
    filme.delete_instance()
    return True
```

**Mudanças:**
- ❌ Sem session
- ✅ .delete_instance() ao invés de session.delete()

---

### 4. Interface Streamlit (`app.py`)

**Antes (SQLAlchemy):**
```python
# TAB: Adicionar
session = get_session()
filme = criar_filme(session, nome, ano, nota)
session.close()

# TAB: Listar
session = get_session()
filmes = listar_filmes(session)
session.close()

# TAB: Atualizar
session = get_session()
filmes = listar_filmes(session)
# ... operações ...
session.close()
```

**Depois (Peewee):**
```python
# TAB: Adicionar
filme = criar_filme(nome, ano, nota)

# TAB: Listar
filmes = listar_filmes()

# TAB: Atualizar
filmes = listar_filmes()
# ... operações ...
# Sem session.close()!
```

**Mudanças:**
- ❌ Sem get_session()
- ❌ Sem session.close()
- ✅ Código muito mais limpo
- ✅ Menos chances de esquecer de fechar sessões

---

## 📊 Comparação de Linhas de Código

| Arquivo | SQLAlchemy | Peewee | Redução |
|---------|------------|--------|---------|
| database.py | ~25 linhas | ~15 linhas | -40% |
| models.py | ~25 linhas | ~20 linhas | -20% |
| crud.py | ~95 linhas | ~85 linhas | -10% |
| app.py | ~160 linhas | ~145 linhas | -9% |
| **Total** | **~305 linhas** | **~265 linhas** | **-13%** |

---

## 🎓 Benefícios Pedagógicos

### Para Estudantes

1. **Menos conceitos** para aprender (sem sessões)
2. **Sintaxe mais intuitiva** (similar ao Django)
3. **Menos código** = menos lugares para errar
4. **Erros mais claros** (DoesNotExist vs None)
5. **Preparação para Django** no futuro

### Para Professores

1. **Mais tempo focando em lógica** ao invés de boilerplate
2. **Menos debugging** de problemas com sessões
3. **Exemplos mais curtos** e fáceis de mostrar
4. **Transição suave** para Django futuramente

---

## 📦 Dependências

**Antes:**
```txt
streamlit==1.29.0
sqlalchemy==2.0.23
```

**Depois:**
```txt
streamlit==1.29.0
peewee==3.17.0
```

---

## 🚀 Como Usar o Novo Material

### Instalação

```bash
cd 4-peewee-orm
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
pip install -r requirements.txt
```

### Executar

```bash
streamlit run app.py
```

### Testar

```python
# No terminal Python
from database import init_db
from crud import criar_filme, listar_filmes

init_db()
filme = criar_filme("Matrix", 1999, 9.0)
print(f"Criado: {filme.nome} (ID: {filme.id})")

filmes = listar_filmes()
for f in filmes:
    print(f"{f.nome} - {f.ano}")
```

---

## 📚 Arquivos Atualizados

- ✅ `database.py` - Configuração simplificada
- ✅ `models.py` - Modelo com class Meta
- ✅ `crud.py` - Funções sem sessão
- ✅ `app.py` - Interface limpa sem gerenciamento de sessão
- ✅ `README.md` - Tutorial completo do Peewee
- ✅ `COMPARACAO.md` - SQL vs Peewee
- ✅ `EXERCICIOS.md` - 15 exercícios adaptados
- ✅ `requirements.txt` - Dependências atualizadas
- ✅ `MIGRACAO.md` - Este arquivo

---

## 💡 Dicas para Ensinar

1. **Comece mostrando a simplicidade**: Compare lado a lado com SQL puro
2. **Destaque a ausência de sessões**: Mostre como isso simplifica
3. **Use o Django como "spoiler"**: "Isso é muito parecido com Django que veremos depois"
4. **Foque nos relacionamentos**: Mostre como é natural navegar entre objetos
5. **Exercícios progressivos**: Do básico ao avançado

---

## 🎯 Próximos Passos

1. Testar todo o material com alunos
2. Coletar feedback sobre dificuldades
3. Criar vídeo-aulas demonstrando Peewee
4. Preparar módulo 5 (Flask) usando Peewee

---

**📝 Observação:** Todos os conceitos de ORM ainda se aplicam, apenas a sintaxe mudou para ser mais simples e acessível!
