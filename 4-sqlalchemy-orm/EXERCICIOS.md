# Exercícios - Módulo 4: SQLAlchemy ORM

## 🎯 Exercícios Básicos

### Exercício 1: Adicionar Campo Gênero
**Objetivo:** Adicionar um novo campo "genero" ao modelo Filme.

**Instruções:**
1. Modifique o modelo `Filme` em `models.py`
2. Adicione uma coluna `genero` do tipo `String`
3. Atualize o `crud.py` para incluir gênero nas operações
4. Atualize a interface do Streamlit

**Dica:**
```python
# Em models.py
genero = Column(String, nullable=True)

# Em crud.py
def criar_filme(session, nome, ano, nota, genero=None):
    filme = Filme(nome=nome, ano=ano, nota=nota, genero=genero)
    # ...
```

---

### Exercício 2: Busca por Gênero
**Objetivo:** Criar função para filtrar filmes por gênero.

**Instruções:**
1. Adicione função `buscar_por_genero()` no `crud.py`
2. Use `session.query(Filme).filter(Filme.genero == genero).all()`
3. Teste com diferentes gêneros

---

### Exercício 3: Contar Filmes
**Objetivo:** Criar função que retorna o total de filmes cadastrados.

**Instruções:**
1. Crie função `contar_filmes(session)` no `crud.py`
2. Use `session.query(Filme).count()`
3. Exiba o resultado na interface

**Dica:**
```python
def contar_filmes(session: Session):
    try:
        total = session.query(Filme).count()
        return total
    except Exception as e:
        print(f"Erro: {e}")
        return 0
```

---

### Exercício 4: Filme com Melhor Nota
**Objetivo:** Buscar o filme com a maior nota cadastrada.

**Instruções:**
1. Crie função `filme_melhor_nota(session)`
2. Use `order_by(Filme.nota.desc()).first()`
3. Exiba na interface com destaque

---

### Exercício 5: Listar Filmes Antigos
**Objetivo:** Filtrar filmes lançados antes de um determinado ano.

**Instruções:**
1. Crie função `filmes_antes_de(session, ano)`
2. Use filtro `Filme.ano < ano`
3. Adicione opção na interface para escolher o ano

---

## 🚀 Exercícios Intermediários

### Exercício 6: Média de Notas
**Objetivo:** Calcular a nota média de todos os filmes.

**Instruções:**
1. Use `from sqlalchemy import func`
2. Crie query: `session.query(func.avg(Filme.nota)).scalar()`
3. Exiba como métrica no Streamlit

**Dica:**
```python
from sqlalchemy import func

def calcular_media_notas(session: Session):
    try:
        media = session.query(func.avg(Filme.nota)).scalar()
        return round(media, 2) if media else 0
    except Exception as e:
        print(f"Erro: {e}")
        return 0
```

---

### Exercício 7: Filmes por Década
**Objetivo:** Agrupar filmes por década e contar quantos há em cada.

**Instruções:**
1. Use agregação do SQLAlchemy
2. Agrupe por década (anos 1990, 2000, 2010, etc.)
3. Exiba em formato de tabela ou gráfico

---

### Exercício 8: Atualização em Lote
**Objetivo:** Criar função para atualizar a nota de vários filmes de uma vez.

**Instruções:**
1. Crie função que recebe lista de IDs
2. Atualize todos com a mesma nota
3. Use `session.query(Filme).filter(Filme.id.in_(ids)).update(...)`

---

### Exercício 9: Paginação
**Objetivo:** Implementar paginação na listagem de filmes.

**Instruções:**
1. Use `limit()` e `offset()` do SQLAlchemy
2. Crie função `listar_filmes_paginados(session, pagina, por_pagina)`
3. Adicione navegação entre páginas no Streamlit

**Dica:**
```python
def listar_filmes_paginados(session, pagina=1, por_pagina=10):
    offset = (pagina - 1) * por_pagina
    filmes = session.query(Filme)\
        .offset(offset)\
        .limit(por_pagina)\
        .all()
    return filmes
```

---

### Exercício 10: Busca Avançada
**Objetivo:** Criar busca com múltiplos filtros combinados.

**Instruções:**
1. Combine filtros de nome, ano e nota
2. Use `and_()` ou `or_()` do SQLAlchemy
3. Permita buscar com critérios opcionais

**Dica:**
```python
from sqlalchemy import and_, or_

filmes = session.query(Filme).filter(
    and_(
        Filme.nome.ilike(f"%{nome}%"),
        Filme.ano >= ano_min,
        Filme.nota >= nota_min
    )
).all()
```

---

## 🏆 Exercícios Avançados

### Exercício 11: Modelo de Diretor
**Objetivo:** Criar um segundo modelo para Diretores.

**Instruções:**
1. Crie classe `Diretor` em `models.py`
2. Campos: id, nome, nacionalidade, data_nascimento
3. Crie operações CRUD para diretores
4. Adicione aba no Streamlit para gerenciar diretores

**Estrutura:**
```python
class Diretor(Base):
    __tablename__ = 'diretores'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    nacionalidade = Column(String)
    data_nascimento = Column(String)
```

---

### Exercício 12: Relacionamento 1:N
**Objetivo:** Criar relacionamento entre Filme e Diretor.

**Instruções:**
1. Adicione campo `diretor_id` em `Filme`
2. Use `ForeignKey` para criar relação
3. Use `relationship()` para navegação
4. Atualize interface para associar filmes a diretores

**Dica:**
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Filme(Base):
    # ... campos existentes ...
    diretor_id = Column(Integer, ForeignKey('diretores.id'))
    
    # Relacionamento
    diretor = relationship("Diretor", back_populates="filmes")

class Diretor(Base):
    # ... campos existentes ...
    filmes = relationship("Filme", back_populates="diretor")
```

---

### Exercício 13: Queries com Join
**Objetivo:** Buscar filmes incluindo informações do diretor.

**Instruções:**
1. Use `join()` para combinar tabelas
2. Busque filmes com nome do diretor
3. Exiba na listagem

**Dica:**
```python
filmes = session.query(Filme)\
    .join(Diretor)\
    .filter(Diretor.nome.ilike(f"%{nome_diretor}%"))\
    .all()
```

---

### Exercício 14: Modelo de Avaliação (N:M)
**Objetivo:** Criar relacionamento muitos-para-muitos entre Filmes e Usuários.

**Instruções:**
1. Crie modelo `Usuario`
2. Crie tabela associativa `avaliacoes`
3. Permita usuários avaliarem filmes
4. Mostre avaliações na interface

**Estrutura:**
```python
from sqlalchemy import Table

# Tabela associativa
avaliacoes = Table('avaliacoes', Base.metadata,
    Column('usuario_id', Integer, ForeignKey('usuarios.id')),
    Column('filme_id', Integer, ForeignKey('filmes.id')),
    Column('nota', Float),
    Column('comentario', String)
)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    filmes_avaliados = relationship("Filme", 
                                   secondary=avaliacoes,
                                   back_populates="avaliadores")
```

---

### Exercício 15: Migrações com Alembic
**Objetivo:** Usar Alembic para gerenciar mudanças no banco.

**Instruções:**
1. Instale: `pip install alembic`
2. Inicialize: `alembic init alembic`
3. Configure `alembic.ini` e `env.py`
4. Crie migração: `alembic revision --autogenerate -m "mensagem"`
5. Aplique: `alembic upgrade head`

**Conceito:** Alembic permite versionar o esquema do banco, facilitando mudanças ao longo do tempo.

---

## 🎓 Projeto Final: Sistema de Biblioteca Completo

**Objetivo:** Criar sistema completo com múltiplos modelos e relacionamentos.

**Requisitos:**

1. **Modelos:**
   - Livro (id, titulo, isbn, ano, disponivel)
   - Autor (id, nome, nacionalidade)
   - Usuario (id, nome, email)
   - Emprestimo (id, livro_id, usuario_id, data_emprestimo, data_devolucao)

2. **Relacionamentos:**
   - Livro N:N Autor (livro pode ter vários autores)
   - Emprestimo N:1 Livro
   - Emprestimo N:1 Usuario

3. **Funcionalidades:**
   - CRUD completo para todos os modelos
   - Registrar empréstimo (marcar livro indisponível)
   - Registrar devolução (marcar livro disponível)
   - Listar livros disponíveis
   - Histórico de empréstimos por usuário
   - Livros mais emprestados
   - Usuários mais ativos

4. **Interface:**
   - Abas separadas para cada entidade
   - Relatórios e estatísticas
   - Busca avançada

---

## 💡 Dicas Gerais

1. **Session Management:**
   - Sempre feche sessões após uso
   - Use try/finally ou context managers

2. **Queries Eficientes:**
   - Use `lazy loading` com cuidado
   - Prefira `joinedload()` para eager loading

3. **Validações:**
   - Valide dados antes de salvar
   - Trate exceções adequadamente

4. **Testes:**
   - Teste cada função isoladamente
   - Use `session.rollback()` em testes

---

## 📚 Recursos de Apoio

- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [SQLAlchemy Relationships](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
- [Query API Reference](https://docs.sqlalchemy.org/en/20/orm/queryguide/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)

---

**Bons estudos e aproveite o poder do SQLAlchemy! 🚀**
