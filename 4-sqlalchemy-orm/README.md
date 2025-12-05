# Módulo 4: SQLAlchemy ORM - Banco de Dados Orientado a Objetos

## 📖 Objetivo

Neste módulo, você aprenderá a trabalhar com banco de dados usando **SQLAlchemy ORM** (Object-Relational Mapping), uma forma mais moderna e orientada a objetos de interagir com bancos de dados, sem precisar escrever SQL diretamente.

Vamos **migrar** nosso sistema de filmes dos módulos anteriores para usar SQLAlchemy!

## 🎯 Conceitos Abordados

- **O que é ORM** (Object-Relational Mapping)
- **SQLAlchemy** - a biblioteca ORM mais popular do Python
- **Modelos como Classes** - representar tabelas como objetos Python
- **Sessions** - gerenciamento de transações
- **Queries orientadas a objetos** - buscar dados sem SQL
- **Relacionamentos** entre tabelas
- **Migração de código** SQLite para SQLAlchemy

## 🤔 Por que usar ORM?

### Comparação: SQL Puro vs SQLAlchemy

**SQL Puro (módulos anteriores):**
```python
cursor.execute("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", 
               (nome, ano, nota))
connection.commit()
```

**SQLAlchemy ORM:**
```python
filme = Filme(nome=nome, ano=ano, nota=nota)
session.add(filme)
session.commit()
```

### Vantagens do ORM:

✅ **Mais Pythônico** - Trabalha com objetos ao invés de strings SQL  
✅ **Menos erros** - O Python detecta erros de sintaxe  
✅ **Portabilidade** - Mesmo código funciona com SQLite, PostgreSQL, MySQL, etc.  
✅ **Segurança** - Proteção automática contra SQL Injection  
✅ **Relacionamentos** - Mais fácil trabalhar com múltiplas tabelas  
✅ **Manutenção** - Código mais limpo e organizado  

### Desvantagens:

⚠️ **Curva de aprendizado** - Conceitos novos para aprender  
⚠️ **Overhead** - Pequena perda de performance (geralmente negligível)  
⚠️ **Queries complexas** - Às vezes SQL puro é mais simples  

## 📋 Pré-requisitos

- Ter concluído os módulos anteriores (especialmente módulo 3)
- Python 3.7 ou superior
- Conhecimento básico de Programação Orientada a Objetos (POO)

---

## 🚀 Passo 1: Instalação do SQLAlchemy

Com o ambiente virtual ativado:

```bash
pip install sqlalchemy
```

Atualize o `requirements.txt`:

```txt
streamlit==1.29.0
sqlalchemy==2.0.23
```

---

## 📁 Passo 2: Estrutura do Projeto

```
4-sqlalchemy-orm/
├── venv/                    # Ambiente virtual
├── models.py                # Modelos SQLAlchemy (nova versão)
├── database.py              # Configuração do banco de dados
├── crud.py                  # Operações CRUD
├── app.py                   # Aplicação Streamlit
├── filmes.db                # Banco de dados SQLite
├── requirements.txt         # Dependências
├── README.md                # Este arquivo
├── EXERCICIOS.md            # Exercícios práticos
└── COMPARACAO.md            # Comparação SQL vs ORM
```

---

## 🏗️ Passo 3: Criando os Modelos

### 3.1 - Arquivo `database.py`

Este arquivo configura a conexão com o banco:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Criar engine de conexão com SQLite
# echo=True mostra os SQL gerados (útil para aprendizado)
engine = create_engine('sqlite:///filmes.db', 
                      echo=False,
                      connect_args={"check_same_thread": False})

# Criar classe base para os modelos
Base = declarative_base()

# Criar fábrica de sessões
SessionLocal = sessionmaker(bind=engine, 
                           autocommit=False, 
                           autoflush=False)

def get_session():
    """Retorna uma nova sessão do banco de dados"""
    return SessionLocal()

def init_db():
    """Inicializa o banco de dados criando todas as tabelas"""
    Base.metadata.create_all(bind=engine)
```

**Explicação:**
- **Engine**: Gerencia a conexão com o banco
- **Base**: Classe pai de todos os modelos
- **SessionLocal**: Fábrica para criar sessões (transações)
- **get_session()**: Função helper para obter sessões
- **init_db()**: Cria as tabelas no banco

### 3.2 - Arquivo `models.py` (Nova versão com ORM)

```python
from sqlalchemy import Column, Integer, String, Float
from database import Base

class Filme(Base):
    """Modelo que representa a tabela de filmes"""
    
    __tablename__ = 'filmes'
    
    # Definição das colunas
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    nota = Column(Float, nullable=False)
    
    def __repr__(self):
        """Representação em string do objeto"""
        return f"<Filme(id={self.id}, nome='{self.nome}', ano={self.ano}, nota={self.nota})>"
    
    def to_dict(self):
        """Converte o objeto para dicionário"""
        return {
            'id': self.id,
            'nome': self.nome,
            'ano': self.ano,
            'nota': self.nota
        }
```

**Explicação:**
- **Class Filme(Base)**: Define uma tabela chamada 'filmes'
- **Column**: Define cada coluna da tabela
- **Integer, String, Float**: Tipos de dados
- **primary_key=True**: Define a chave primária
- **nullable=False**: Campo obrigatório
- **__repr__()**: Como o objeto é exibido no print()
- **to_dict()**: Converte objeto para dicionário (útil para Streamlit)

---

## 🔧 Passo 4: Operações CRUD com SQLAlchemy

Vamos criar um arquivo `crud.py` com as operações:

```python
from sqlalchemy.orm import Session
from models import Filme

def criar_filme(session: Session, nome: str, ano: int, nota: float):
    """Cria um novo filme no banco de dados"""
    try:
        filme = Filme(nome=nome, ano=ano, nota=nota)
        session.add(filme)
        session.commit()
        session.refresh(filme)  # Atualiza o objeto com dados do banco (ex: ID)
        return filme
    except Exception as e:
        session.rollback()
        print(f"Erro ao criar filme: {e}")
        return None

def listar_filmes(session: Session):
    """Lista todos os filmes ordenados por ano (decrescente)"""
    try:
        filmes = session.query(Filme).order_by(Filme.ano.desc()).all()
        return filmes
    except Exception as e:
        print(f"Erro ao listar filmes: {e}")
        return []

def buscar_filme_por_id(session: Session, filme_id: int):
    """Busca um filme pelo ID"""
    try:
        filme = session.query(Filme).filter(Filme.id == filme_id).first()
        return filme
    except Exception as e:
        print(f"Erro ao buscar filme: {e}")
        return None

def atualizar_filme(session: Session, filme_id: int, nome: str = None, 
                   ano: int = None, nota: float = None):
    """Atualiza os dados de um filme"""
    try:
        filme = buscar_filme_por_id(session, filme_id)
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
        print(f"Erro ao atualizar filme: {e}")
        return False

def deletar_filme(session: Session, filme_id: int):
    """Deleta um filme pelo ID"""
    try:
        filme = buscar_filme_por_id(session, filme_id)
        if not filme:
            return False
        
        session.delete(filme)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        print(f"Erro ao deletar filme: {e}")
        return False

def buscar_por_nome(session: Session, nome: str):
    """Busca filmes por nome (busca parcial)"""
    try:
        filmes = session.query(Filme).filter(
            Filme.nome.ilike(f"%{nome}%")
        ).all()
        return filmes
    except Exception as e:
        print(f"Erro ao buscar por nome: {e}")
        return []

def filtrar_por_ano(session: Session, ano_min: int, ano_max: int):
    """Filtra filmes por intervalo de anos"""
    try:
        filmes = session.query(Filme).filter(
            Filme.ano >= ano_min,
            Filme.ano <= ano_max
        ).all()
        return filmes
    except Exception as e:
        print(f"Erro ao filtrar por ano: {e}")
        return []
```

---

## 💻 Passo 5: Atualizando a Aplicação Streamlit

Arquivo `app.py` atualizado:

```python
import streamlit as st
from database import get_session, init_db
from crud import (
    criar_filme, 
    listar_filmes, 
    buscar_filme_por_id, 
    atualizar_filme, 
    deletar_filme
)

# Configuração da página
st.set_page_config(
    page_title="Sistema de Filmes - SQLAlchemy",
    page_icon="🎬",
    layout="wide",
)

# Inicializar banco de dados
init_db()

# Título principal
st.title("🎬 Sistema de Filmes - SQLAlchemy ORM")
st.markdown("---")

# Criar abas
tab1, tab2, tab3, tab4 = st.tabs(["Adicionar", "Listar", "Atualizar", "Deletar"])

# TAB 1: Adicionar Filme
with tab1:
    st.subheader("Adicionar Novo Filme")
    
    nome = st.text_input("Nome do Filme")
    ano = st.number_input("Ano", min_value=1900, max_value=2030, value=2024)
    nota = st.slider("Nota", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    
    if st.button("Adicionar"):
        if nome.strip():
            session = get_session()
            filme = criar_filme(session, nome, ano, nota)
            session.close()
            
            if filme:
                st.success(f"Filme '{nome}' adicionado com sucesso! (ID: {filme.id})")
                st.balloons()
            else:
                st.error("Erro ao adicionar filme.")
        else:
            st.error("O nome do filme não pode estar vazio.")

# TAB 2: Listar Filmes
with tab2:
    st.subheader("Lista de Filmes")
    
    session = get_session()
    filmes = listar_filmes(session)
    session.close()
    
    if filmes:
        st.write(f"Total de filmes: {len(filmes)}")
        
        for filme in filmes:
            st.write(f"**ID:** {filme.id} | **Nome:** {filme.nome} | "
                    f"**Ano:** {filme.ano} | **Nota:** {filme.nota}")
    else:
        st.info("Nenhum filme cadastrado.")

# TAB 3: Atualizar Filme
with tab3:
    st.subheader("Atualizar Filme")
    
    session = get_session()
    filmes = listar_filmes(session)
    
    if filmes:
        filmes_dict = {f"{f.id} - {f.nome}": f.id for f in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para atualizar",
            options=list(filmes_dict.keys())
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = buscar_filme_por_id(session, filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.write(f"**Filme atual:** {filme_atual.nome} ({filme_atual.ano}) - "
                        f"Nota: {filme_atual.nota}")
                
                novo_nome = st.text_input("Novo Nome", value=filme_atual.nome)
                novo_ano = st.number_input("Novo Ano", min_value=1900, 
                                          max_value=2030, value=filme_atual.ano)
                nova_nota = st.slider("Nova Nota", min_value=0.0, max_value=10.0, 
                                    value=float(filme_atual.nota), step=0.1)
                
                if st.button("Salvar Alterações"):
                    if novo_nome.strip():
                        if atualizar_filme(session, filme_id, novo_nome, novo_ano, nova_nota):
                            st.success("Filme atualizado com sucesso!")
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar filme.")
                    else:
                        st.error("O nome do filme não pode estar vazio.")
    else:
        st.info("Nenhum filme cadastrado.")
    
    session.close()

# TAB 4: Deletar Filme
with tab4:
    st.subheader("Deletar Filme")
    
    session = get_session()
    filmes = listar_filmes(session)
    
    if filmes:
        filmes_dict = {f"{f.id} - {f.nome}": f.id for f in filmes}
        
        filme_selecionado = st.selectbox(
            "Selecione o filme para deletar",
            options=list(filmes_dict.keys()),
            key="delete_select"
        )
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = buscar_filme_por_id(session, filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.warning(f"Você está prestes a deletar: **{filme_atual.nome} "
                          f"({filme_atual.ano})**")
                
                if st.button("Confirmar Exclusão", type="primary"):
                    if deletar_filme(session, filme_id):
                        st.success(f"Filme '{filme_atual.nome}' deletado com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao deletar filme.")
    else:
        st.info("Nenhum filme cadastrado.")
    
    session.close()

# Rodapé
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>💡 Sistema desenvolvido com SQLAlchemy ORM | 📚 Programação com Banco de Dados</p>
    </div>
    """,
    unsafe_allow_html=True
)
```

---

## 📊 Comparação: Antes vs Depois

### Antes (SQLite Puro):
```python
# Criar filme
cursor.execute("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", 
               (nome, ano, nota))
connection.commit()

# Listar filmes
cursor.execute("SELECT id, nome, ano, nota FROM filmes ORDER BY ano DESC")
filmes = cursor.fetchall()
```

### Depois (SQLAlchemy):
```python
# Criar filme
filme = Filme(nome=nome, ano=ano, nota=nota)
session.add(filme)
session.commit()

# Listar filmes
filmes = session.query(Filme).order_by(Filme.ano.desc()).all()
```

---

## 🎓 Conceitos Importantes

### Session (Sessão)
- Gerencia transações com o banco
- Deve ser criada, usada e fechada
- Similar a uma "conversa" com o banco de dados

```python
session = get_session()  # Abre sessão
# ... operações ...
session.close()  # Fecha sessão
```

### Query (Consulta)
- Busca dados de forma orientada a objetos
- Métodos encadeáveis

```python
# Filtrar
filmes = session.query(Filme).filter(Filme.ano > 2000).all()

# Ordenar
filmes = session.query(Filme).order_by(Filme.nome).all()

# Limitar
filmes = session.query(Filme).limit(10).all()

# Buscar um
filme = session.query(Filme).filter(Filme.id == 1).first()

# Contar
total = session.query(Filme).count()
```

### Commit e Rollback
- **commit()**: Salva as alterações no banco
- **rollback()**: Desfaz alterações em caso de erro

```python
try:
    session.add(filme)
    session.commit()  # Salva
except:
    session.rollback()  # Desfaz
```

---

## 🚀 Executando a Aplicação

```bash
# Ativar ambiente virtual
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Executar aplicação
streamlit run app.py
```

---

## 🎯 Exercícios

Veja o arquivo `EXERCICIOS.md` para atividades práticas!

---

## 📚 Próximos Passos

No próximo módulo, você aprenderá sobre:
- **Flask** - Framework web completo
- **APIs REST** - Criar endpoints HTTP
- **Autenticação** - Login e segurança
- **Deploy** - Colocar aplicação online

---

## 📖 Recursos Adicionais

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [SQLAlchemy Query API](https://docs.sqlalchemy.org/en/20/orm/queryguide/)

---

**Bons estudos e aproveite o poder do ORM! 🚀**