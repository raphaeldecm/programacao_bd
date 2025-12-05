# Módulo 4: Peewee ORM - Banco de Dados Orientado a Objetos

## 📖 Objetivo

Neste módulo, você aprenderá a trabalhar com banco de dados usando **Peewee ORM** (Object-Relational Mapping), uma forma mais moderna, simples e orientada a objetos de interagir com bancos de dados, sem precisar escrever SQL diretamente.

Vamos **migrar** nosso sistema de filmes dos módulos anteriores para usar Peewee!

## 🎯 Conceitos Abordados

- **O que é ORM** (Object-Relational Mapping)
- **Peewee** - ORM simples e intuitivo (similar ao Django ORM)
- **Modelos como Classes** - representar tabelas como objetos Python
- **Queries orientadas a objetos** - buscar dados sem SQL
- **Relacionamentos** entre tabelas
- **Migração de código** SQLite para Peewee

## 🤔 Por que usar ORM?

### Comparação: SQL Puro vs Peewee

**SQL Puro (módulos anteriores):**

```python
cursor.execute("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", 
               (nome, ano, nota))
connection.commit()
```

**Peewee ORM:**

```python
filme = Filme.create(nome=nome, ano=ano, nota=nota)
```

### Vantagens do ORM

✅ **Mais Pythônico** - Trabalha com objetos ao invés de strings SQL  
✅ **Menos erros** - O Python detecta erros de sintaxe  
✅ **Portabilidade** - Mesmo código funciona com SQLite, PostgreSQL, MySQL, etc.  
✅ **Segurança** - Proteção automática contra SQL Injection  
✅ **Relacionamentos** - Mais fácil trabalhar com múltiplas tabelas  
✅ **Manutenção** - Código mais limpo e organizado  
✅ **Simplicidade** - Sintaxe simples e intuitiva, similar ao Django ORM

### Desvantagens

⚠️ **Curva de aprendizado** - Conceitos novos para aprender  
⚠️ **Overhead** - Pequena perda de performance (geralmente negligível)  
⚠️ **Queries complexas** - Às vezes SQL puro é mais simples  

## 🌟 Por que Peewee ao invés de SQLAlchemy?

- ✅ **Mais simples** - Menos boilerplate, código mais direto
- ✅ **Similar ao Django** - Preparação para frameworks web modernos
- ✅ **Menos conceitos** - Não precisa gerenciar sessões manualmente
- ✅ **Mais leve** - Menor footprint de memória
- ✅ **Documentação clara** - Fácil para iniciantes
- ✅ **Código limpo** - Menos linhas de código para mesma funcionalidade

## 📋 Pré-requisitos

- Ter concluído os módulos anteriores (especialmente módulo 3)
- Python 3.7 ou superior
- Conhecimento básico de Programação Orientada a Objetos (POO)

---

## 🚀 Passo 1: Instalação do Peewee

Com o ambiente virtual ativado:

```bash
pip install peewee
```

Atualize o `requirements.txt`:

```txt
streamlit==1.29.0
peewee==3.17.0
```

---

## 📁 Passo 2: Estrutura do Projeto

```
4-peewee-orm/
├── venv/                    # Ambiente virtual
├── models.py                # Modelos Peewee (nova versão)
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
from peewee import SqliteDatabase

# Criar conexão com o banco de dados SQLite
# pragmas ajudam com performance e compatibilidade
db = SqliteDatabase('filmes.db', pragmas={
    'journal_mode': 'wal',  # Write-Ahead Logging para melhor concorrência
    'cache_size': -1024 * 64,  # 64MB de cache
    'foreign_keys': 1,  # Habilitar chaves estrangeiras
    'ignore_check_constraints': 0,
    'synchronous': 0
})

def init_db():
    """Inicializa o banco de dados criando todas as tabelas"""
    from models import Filme
    db.connect()
    db.create_tables([Filme], safe=True)
    
def close_db():
    """Fecha a conexão com o banco de dados"""
    if not db.is_closed():
        db.close()
```

**Explicação:**

- **SqliteDatabase**: Cria conexão com SQLite
- **pragmas**: Otimizações de performance
- **init_db()**: Cria as tabelas (safe=True evita erro se já existir)
- **close_db()**: Fecha conexão quando necessário

### 3.2 - Arquivo `models.py` (Nova versão com ORM)

```python
from peewee import Model, AutoField, CharField, IntegerField, FloatField
from database import db

class Filme(Model):
    """Modelo que representa a tabela de filmes"""
    
    # Definição das colunas
    id = AutoField(primary_key=True)  # Auto-incremento automático
    nome = CharField(null=False)
    ano = IntegerField(null=False)
    nota = FloatField(null=False)
    
    class Meta:
        database = db  # Conexão com o banco
        table_name = 'filmes'  # Nome da tabela
    
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

- **Model**: Classe base do Peewee para modelos
- **AutoField**: Campo auto-incremento para ID
- **CharField, IntegerField, FloatField**: Tipos de campo
- **null=False**: Campo obrigatório
- **class Meta**: Metadados do modelo (banco e nome da tabela)
- **\_\_repr\_\_()**: Como o objeto é exibido no print()
- **to_dict()**: Converte objeto para dicionário (útil para Streamlit)

---

## 🔧 Passo 4: Operações CRUD com Peewee

Vamos criar um arquivo `crud.py` com as operações:

```python
from models import Filme
from peewee import DoesNotExist

def criar_filme(nome: str, ano: int, nota: float):
    """Cria um novo filme no banco de dados"""
    try:
        filme = Filme.create(nome=nome, ano=ano, nota=nota)
        return filme
    except Exception as e:
        print(f"Erro ao criar filme: {e}")
        return None

def listar_filmes():
    """Lista todos os filmes ordenados por ano (decrescente)"""
    try:
        filmes = Filme.select().order_by(Filme.ano.desc())
        return list(filmes)
    except Exception as e:
        print(f"Erro ao listar filmes: {e}")
        return []

def buscar_filme_por_id(filme_id: int):
    """Busca um filme pelo ID"""
    try:
        filme = Filme.get_by_id(filme_id)
        return filme
    except DoesNotExist:
        return None
    except Exception as e:
        print(f"Erro ao buscar filme: {e}")
        return None

def atualizar_filme(filme_id: int, nome: str = None, 
                   ano: int = None, nota: float = None):
    """Atualiza os dados de um filme"""
    try:
        filme = buscar_filme_por_id(filme_id)
        if not filme:
            return False
        
        # Atualizar apenas os campos fornecidos
        if nome is not None:
            filme.nome = nome
        if ano is not None:
            filme.ano = ano
        if nota is not None:
            filme.nota = nota
        
        filme.save()  # Salvar alterações
        return True
    except Exception as e:
        print(f"Erro ao atualizar filme: {e}")
        return False

def deletar_filme(filme_id: int):
    """Deleta um filme pelo ID"""
    try:
        filme = buscar_filme_por_id(filme_id)
        if not filme:
            return False
        
        filme.delete_instance()
        return True
    except Exception as e:
        print(f"Erro ao deletar filme: {e}")
        return False

def buscar_por_nome(nome: str):
    """Busca filmes por nome (busca parcial, case-insensitive)"""
    try:
        filmes = Filme.select().where(
            Filme.nome.contains(nome)
        )
        return list(filmes)
    except Exception as e:
        print(f"Erro ao buscar por nome: {e}")
        return []

def filtrar_por_ano(ano_min: int, ano_max: int):
    """Filtra filmes por intervalo de anos"""
    try:
        filmes = Filme.select().where(
            (Filme.ano >= ano_min) & (Filme.ano <= ano_max)
        )
        return list(filmes)
    except Exception as e:
        print(f"Erro ao filtrar por ano: {e}")
        return []
```

**Vantagens do Peewee:**

- **Menos código**: `Filme.create()` ao invés de criar objeto, add, commit
- **Mais simples**: `filme.save()` ao invés de session.commit()
- **Mais direto**: `Filme.get_by_id()` ao invés de query().filter().first()
- **Sem sessões**: Não precisa gerenciar sessões manualmente

---

## 💻 Passo 5: Atualizando a Aplicação Streamlit

Arquivo `app.py` atualizado - veja como ficou simples sem gerenciar sessões:

```python
import streamlit as st
from database import init_db
from crud import criar_filme, listar_filmes, buscar_filme_por_id, atualizar_filme, deletar_filme

# Configuração e inicialização
st.set_page_config(page_title="Sistema de Filmes - Peewee ORM", page_icon="🎬", layout="wide")
init_db()

st.title("🎬 Sistema de Filmes - Peewee ORM")
st.markdown("---")

# Abas
tab1, tab2, tab3, tab4 = st.tabs(["Adicionar", "Listar", "Atualizar", "Deletar"])

# TAB 1: Adicionar
with tab1:
    st.subheader("Adicionar Novo Filme")
    nome = st.text_input("Nome do Filme")
    ano = st.number_input("Ano", min_value=1900, max_value=2030, value=2024)
    nota = st.slider("Nota", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
    
    if st.button("Adicionar"):
        if nome.strip():
            filme = criar_filme(nome, ano, nota)  # Sem session!
            if filme:
                st.success(f"Filme '{nome}' adicionado! (ID: {filme.id})")
                st.balloons()
            else:
                st.error("Erro ao adicionar filme.")
        else:
            st.error("O nome não pode estar vazio.")

# TAB 2: Listar
with tab2:
    st.subheader("Lista de Filmes")
    filmes = listar_filmes()  # Sem session!
    
    if filmes:
        st.write(f"Total: {len(filmes)}")
        for filme in filmes:
            st.write(f"**ID:** {filme.id} | **Nome:** {filme.nome} | "
                    f"**Ano:** {filme.ano} | **Nota:** {filme.nota}")
    else:
        st.info("Nenhum filme cadastrado.")

# TAB 3: Atualizar
with tab3:
    st.subheader("Atualizar Filme")
    filmes = listar_filmes()
    
    if filmes:
        filmes_dict = {f"{f.id} - {f.nome}": f.id for f in filmes}
        filme_selecionado = st.selectbox("Selecione o filme", list(filmes_dict.keys()))
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = buscar_filme_por_id(filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.write(f"**Filme atual:** {filme_atual.nome} ({filme_atual.ano}) - Nota: {filme_atual.nota}")
                
                novo_nome = st.text_input("Novo Nome", value=filme_atual.nome)
                novo_ano = st.number_input("Novo Ano", min_value=1900, max_value=2030, value=filme_atual.ano)
                nova_nota = st.slider("Nova Nota", min_value=0.0, max_value=10.0, value=float(filme_atual.nota), step=0.1)
                
                if st.button("Salvar Alterações"):
                    if novo_nome.strip():
                        if atualizar_filme(filme_id, novo_nome, novo_ano, nova_nota):
                            st.success("Filme atualizado!")
                            st.rerun()
                        else:
                            st.error("Erro ao atualizar.")
                    else:
                        st.error("Nome não pode estar vazio.")
    else:
        st.info("Nenhum filme cadastrado.")

# TAB 4: Deletar
with tab4:
    st.subheader("Deletar Filme")
    filmes = listar_filmes()
    
    if filmes:
        filmes_dict = {f"{f.id} - {f.nome}": f.id for f in filmes}
        filme_selecionado = st.selectbox("Selecione o filme", list(filmes_dict.keys()), key="delete_select")
        
        if filme_selecionado:
            filme_id = filmes_dict[filme_selecionado]
            filme_atual = buscar_filme_por_id(filme_id)
            
            if filme_atual:
                st.markdown("---")
                st.warning(f"Deletar: **{filme_atual.nome} ({filme_atual.ano})**")
                
                if st.button("Confirmar Exclusão", type="primary"):
                    if deletar_filme(filme_id):
                        st.success(f"Filme '{filme_atual.nome}' deletado!")
                        st.rerun()
                    else:
                        st.error("Erro ao deletar.")
    else:
        st.info("Nenhum filme cadastrado.")

# Rodapé
st.markdown("---")
st.markdown("<div style='text-align: center'><p>💡 Sistema com Peewee ORM | 📚 Programação com Banco de Dados</p></div>", unsafe_allow_html=True)
```

**Observe a simplicidade:**

- ❌ Não precisa de `get_session()`
- ❌ Não precisa de `session.close()`
- ❌ Não precisa de `session.commit()`
- ✅ Código mais limpo e direto!

---

## 📊 Comparação: Antes vs Depois

### Antes (SQLite Puro)

```python
# Criar filme
cursor.execute("INSERT INTO filmes (nome, ano, nota) VALUES (?, ?, ?)", 
               (nome, ano, nota))
connection.commit()

# Listar filmes
cursor.execute("SELECT id, nome, ano, nota FROM filmes ORDER BY ano DESC")
filmes = cursor.fetchall()
for filme in filmes:
    print(filme[1])  # Índice numérico!
```

### Depois (Peewee ORM)

```python
# Criar filme
filme = Filme.create(nome=nome, ano=ano, nota=nota)

# Listar filmes
filmes = Filme.select().order_by(Filme.ano.desc())
for filme in filmes:
    print(filme.nome)  # Atributo nomeado!
```

---

## 🎓 Conceitos Importantes do Peewee

### 1. Queries Encadeáveis

```python
# Filtrar
filmes = Filme.select().where(Filme.ano > 2000)

# Ordenar
filmes = Filme.select().order_by(Filme.nome)

# Limitar
filmes = Filme.select().limit(10)

# Combinar
filmes = (Filme
          .select()
          .where(Filme.ano > 2000)
          .order_by(Filme.nota.desc())
          .limit(5))
```

### 2. CRUD Simplificado

```python
# CREATE
filme = Filme.create(nome="Inception", ano=2010, nota=9.5)

# READ
filme = Filme.get_by_id(1)
filmes = Filme.select()

# UPDATE
filme.nome = "Inception - Edição Especial"
filme.save()

# DELETE
filme.delete_instance()
```

### 3. Operadores de Filtro

```python
# Igualdade
Filme.select().where(Filme.ano == 2020)

# Maior/Menor
Filme.select().where(Filme.nota > 8.0)
Filme.select().where(Filme.ano < 2000)

# Entre (BETWEEN)
Filme.select().where(Filme.ano.between(2000, 2020))

# Contém (LIKE)
Filme.select().where(Filme.nome.contains("Matrix"))

# Começa/Termina com
Filme.select().where(Filme.nome.startswith("The"))
Filme.select().where(Filme.nome.endswith("Wars"))

# IN
Filme.select().where(Filme.ano.in_([2020, 2021, 2022]))

# Múltiplos filtros (AND)
Filme.select().where(
    (Filme.ano > 2000) & (Filme.nota > 8.0)
)

# OU (OR)
Filme.select().where(
    (Filme.ano < 1990) | (Filme.ano > 2020)
)
```

### 4. Agregações e Estatísticas

```python
from peewee import fn

# Contar
total = Filme.select().count()

# Média
media_nota = Filme.select(fn.AVG(Filme.nota)).scalar()

# Máximo/Mínimo
melhor_nota = Filme.select(fn.MAX(Filme.nota)).scalar()
pior_nota = Filme.select(fn.MIN(Filme.nota)).scalar()

# Soma
soma_notas = Filme.select(fn.SUM(Filme.nota)).scalar()

# Agrupar
filmes_por_ano = (Filme
                  .select(Filme.ano, fn.COUNT(Filme.id).alias('total'))
                  .group_by(Filme.ano))
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

## 🆚 Peewee vs SQLAlchemy: Comparação Rápida

| Característica | Peewee | SQLAlchemy |
|----------------|--------|------------|
| **Simplicidade** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |
| **Curva de aprendizado** | Baixa | Média/Alta |
| **Linhas de código** | Menos | Mais |
| **Gerenciamento de sessões** | Automático | Manual |
| **Sintaxe** | Django-like | Própria |
| **Performance** | Ótima | Excelente |
| **Recursos avançados** | Bom | Excelente |
| **Comunidade** | Menor | Maior |
| **Documentação** | Boa | Excelente |
| **Melhor para** | Projetos pequenos/médios | Projetos grandes/complexos |

---

## 🎯 Exercícios

Veja o arquivo `EXERCICIOS.md` para atividades práticas!

Veja também `COMPARACAO.md` para exemplos lado a lado de SQL vs Peewee.

---

## 📚 Próximos Passos

No próximo módulo (Flask), você aprenderá sobre:

- **Flask** - Framework web completo
- **APIs REST** - Criar endpoints HTTP
- **Autenticação** - Login e segurança
- **Deploy** - Colocar aplicação online

---

## 💡 Dicas Importantes

1. **Use `safe=True`** ao criar tabelas para evitar erros se já existirem
2. **DoesNotExist** é mais específico que Exception para buscar por ID
3. **`.save()`** atualiza apenas campos modificados (eficiente!)
4. **Queries são lazy** - só executam quando você itera ou chama `.execute()`
5. **Use `list()`** para converter queries em listas quando necessário

---

## 📖 Recursos Adicionais

- [Peewee Documentation](http://docs.peewee-orm.com/)
- [Peewee Quickstart](http://docs.peewee-orm.com/en/latest/peewee/quickstart.html)
- [Peewee Querying](http://docs.peewee-orm.com/en/latest/peewee/querying.html)
- [Peewee Models](http://docs.peewee-orm.com/en/latest/peewee/models.html)

---

**🎉 Parabéns! Você agora sabe trabalhar com ORM em Python!**
