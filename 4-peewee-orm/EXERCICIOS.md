# Exercícios - Módulo 4: Peewee ORM

## 🎯 Exercícios Básicos

### Exercício 1: Adicionar Campo Gênero

**Objetivo:** Adicionar um novo campo "genero" ao modelo Filme.

**Instruções:**

1. Modifique o modelo `Filme` em `models.py`
2. Adicione uma coluna `genero` do tipo `CharField`
3. Atualize o `crud.py` para incluir gênero nas operações
4. Atualize a interface do Streamlit

**Dica:**

```python
# Em models.py
class Filme(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    ano = IntegerField(null=False)
    nota = FloatField(null=False)
    genero = CharField(null=True)  # Nova coluna
    
    class Meta:
        database = db
        table_name = 'filmes'

# Em crud.py
def criar_filme(nome, ano, nota, genero=None):
    filme = Filme.create(nome=nome, ano=ano, nota=nota, genero=genero)
    return filme
```

---

### Exercício 2: Busca por Gênero

**Objetivo:** Criar função para filtrar filmes por gênero.

**Instruções:**

1. Adicione função `buscar_por_genero()` no `crud.py`
2. Use `Filme.select().where(Filme.genero == genero)`
3. Teste com diferentes gêneros

**Solução:**

```python
def buscar_por_genero(genero: str):
    try:
        filmes = Filme.select().where(Filme.genero == genero)
        return list(filmes)
    except Exception as e:
        print(f"Erro: {e}")
        return []
```

---

### Exercício 3: Contar Filmes

**Objetivo:** Criar função que retorna o total de filmes cadastrados.

**Instruções:**

1. Crie função `contar_filmes()` no `crud.py`
2. Use `Filme.select().count()`
3. Exiba o resultado na interface

**Dica:**

```python
def contar_filmes():
    try:
        return Filme.select().count()
    except Exception as e:
        print(f"Erro: {e}")
        return 0
```

---

### Exercício 4: Filme com Melhor Nota

**Objetivo:** Buscar o filme com a maior nota cadastrada.

**Instruções:**

1. Crie função `filme_melhor_nota()`
2. Use `Filme.select().order_by(Filme.nota.desc()).first()`
3. Exiba na interface com destaque

**Solução:**

```python
def filme_melhor_nota():
    try:
        return Filme.select().order_by(Filme.nota.desc()).first()
    except Exception as e:
        print(f"Erro: {e}")
        return None
```

---

### Exercício 5: Listar Filmes Antigos

**Objetivo:** Filtrar filmes lançados antes de um determinado ano.

**Instruções:**

1. Crie função `filmes_antes_de(ano)`
2. Use filtro `Filme.ano < ano`
3. Adicione opção na interface para escolher o ano

**Dica:**

```python
def filmes_antes_de(ano: int):
    try:
        filmes = Filme.select().where(Filme.ano < ano)
        return list(filmes)
    except Exception as e:
        print(f"Erro: {e}")
        return []
```

---

## 🚀 Exercícios Intermediários

### Exercício 6: Média de Notas

**Objetivo:** Calcular a nota média de todos os filmes.

**Instruções:**

1. Use `from peewee import fn`
2. Crie query: `Filme.select(fn.AVG(Filme.nota)).scalar()`
3. Exiba como métrica no Streamlit

**Dica:**

```python
from peewee import fn

def calcular_media_notas():
    try:
        media = Filme.select(fn.AVG(Filme.nota)).scalar()
        return round(media, 2) if media else 0
    except Exception as e:
        print(f"Erro: {e}")
        return 0
```

---

### Exercício 7: Top 5 Filmes

**Objetivo:** Listar os 5 filmes com melhores notas.

**Instruções:**

1. Use `.order_by(Filme.nota.desc()).limit(5)`
2. Exiba em formato de ranking
3. Use emojis para destacar (🥇🥈🥉)

**Solução:**

```python
def top_filmes(limite=5):
    try:
        filmes = (Filme.select()
                  .order_by(Filme.nota.desc())
                  .limit(limite))
        return list(filmes)
    except Exception as e:
        print(f"Erro: {e}")
        return []
```

---

### Exercício 8: Filmes por Década

**Objetivo:** Agrupar e contar filmes por década.

**Instruções:**

1. Use operações matemáticas: `(Filme.ano // 10) * 10`
2. Use `group_by` e `fn.COUNT`
3. Exiba em gráfico de barras no Streamlit

**Dica:**

```python
from peewee import fn

def filmes_por_decada():
    try:
        decadas = (Filme
                   .select((Filme.ano // 10 * 10).alias('decada'),
                          fn.COUNT(Filme.id).alias('total'))
                   .group_by(Filme.ano // 10 * 10)
                   .order_by(Filme.ano // 10 * 10))
        return list(decadas)
    except Exception as e:
        print(f"Erro: {e}")
        return []
```

---

### Exercício 9: Busca Flexível

**Objetivo:** Criar busca que aceita múltiplos critérios opcionais.

**Instruções:**

1. Aceite nome, ano_min, ano_max, nota_min como parâmetros opcionais
2. Construa query dinamicamente
3. Adicione interface com múltiplos filtros

**Solução:**

```python
def busca_avancada(nome=None, ano_min=None, ano_max=None, nota_min=None):
    try:
        query = Filme.select()
        
        if nome:
            query = query.where(Filme.nome.contains(nome))
        if ano_min:
            query = query.where(Filme.ano >= ano_min)
        if ano_max:
            query = query.where(Filme.ano <= ano_max)
        if nota_min:
            query = query.where(Filme.nota >= nota_min)
        
        return list(query)
    except Exception as e:
        print(f"Erro: {e}")
        return []
```

---

### Exercício 10: Validação de Dados

**Objetivo:** Adicionar validações antes de salvar filmes.

**Instruções:**

1. Valide que o ano está entre 1895 e ano atual + 5
2. Valide que a nota está entre 0 e 10
3. Valide que o nome tem pelo menos 2 caracteres
4. Retorne mensagens de erro específicas

**Dica:**

```python
from datetime import datetime

def validar_filme(nome, ano, nota):
    erros = []
    
    if len(nome.strip()) < 2:
        erros.append("Nome deve ter pelo menos 2 caracteres")
    
    ano_atual = datetime.now().year
    if ano < 1895 or ano > ano_atual + 5:
        erros.append(f"Ano deve estar entre 1895 e {ano_atual + 5}")
    
    if nota < 0 or nota > 10:
        erros.append("Nota deve estar entre 0 e 10")
    
    return erros

def criar_filme_validado(nome, ano, nota):
    erros = validar_filme(nome, ano, nota)
    if erros:
        return None, erros
    
    try:
        filme = Filme.create(nome=nome, ano=ano, nota=nota)
        return filme, []
    except Exception as e:
        return None, [str(e)]
```

---

## 🔥 Exercícios Avançados

### Exercício 11: Modelo de Diretor com Relacionamento

**Objetivo:** Criar tabela de diretores e relacionar com filmes (1:N).

**Instruções:**

1. Crie modelo `Diretor` em `models.py`
2. Adicione `ForeignKeyField` em `Filme` apontando para `Diretor`
3. Use `backref='filmes'` para acesso reverso
4. Atualize CRUD e interface

**Solução:**

```python
# Em models.py
class Diretor(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    nacionalidade = CharField(null=True)
    
    class Meta:
        database = db
        table_name = 'diretores'

class Filme(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    ano = IntegerField(null=False)
    nota = FloatField(null=False)
    diretor = ForeignKeyField(Diretor, backref='filmes', null=True)
    
    class Meta:
        database = db
        table_name = 'filmes'

# Usar
diretor = Diretor.create(nome="Christopher Nolan", nacionalidade="Britânico")
filme = Filme.create(nome="Inception", ano=2010, nota=9.5, diretor=diretor)

# Acessar
print(filme.diretor.nome)  # Christopher Nolan
for f in diretor.filmes:  # Todos os filmes do diretor
    print(f.nome)
```

---

### Exercício 12: Modelo de Ator com Relacionamento N:M

**Objetivo:** Criar tabela de atores com relacionamento muitos-para-muitos.

**Instruções:**

1. Crie modelo `Ator`
2. Crie modelo intermediário `FilmeAtor`
3. Implemente funções para adicionar atores a filmes

**Solução:**

```python
# Em models.py
class Ator(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False)
    
    class Meta:
        database = db
        table_name = 'atores'

class FilmeAtor(Model):
    filme = ForeignKeyField(Filme, backref='elenco')
    ator = ForeignKeyField(Ator, backref='filmografia')
    personagem = CharField(null=True)  # Nome do personagem
    
    class Meta:
        database = db
        table_name = 'filmes_atores'
        primary_key = False  # Chave composta

# Usar
ator = Ator.create(nome="Leonardo DiCaprio")
filme = Filme.get_by_id(1)
FilmeAtor.create(filme=filme, ator=ator, personagem="Dom Cobb")

# Listar atores de um filme
filme = Filme.get_by_id(1)
for fa in filme.elenco:
    print(f"{fa.ator.nome} como {fa.personagem}")

# Listar filmes de um ator
ator = Ator.get_by_id(1)
for fa in ator.filmografia:
    print(fa.filme.nome)
```

---

### Exercício 13: Estatísticas Avançadas

**Objetivo:** Criar dashboard com estatísticas diversas.

**Instruções:**

1. Total de filmes
2. Nota média geral
3. Filme mais recente
4. Filme mais antigo
5. Distribuição de notas (quantos filmes em cada faixa)
6. Exiba em colunas no Streamlit

**Dica:**

```python
def obter_estatisticas():
    return {
        'total': Filme.select().count(),
        'media_nota': Filme.select(fn.AVG(Filme.nota)).scalar() or 0,
        'melhor_nota': Filme.select(fn.MAX(Filme.nota)).scalar() or 0,
        'pior_nota': Filme.select(fn.MIN(Filme.nota)).scalar() or 0,
        'mais_recente': Filme.select().order_by(Filme.ano.desc()).first(),
        'mais_antigo': Filme.select().order_by(Filme.ano.asc()).first(),
    }
```

---

### Exercício 14: Exportar para CSV/JSON

**Objetivo:** Adicionar funcionalidade de exportar dados.

**Instruções:**

1. Crie função para exportar filmes para CSV
2. Crie função para exportar para JSON
3. Use `st.download_button` no Streamlit
4. Inclua opção de filtrar antes de exportar

**Solução:**

```python
import csv
import json
from io import StringIO

def exportar_csv():
    filmes = Filme.select()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['ID', 'Nome', 'Ano', 'Nota'])
    
    for filme in filmes:
        writer.writerow([filme.id, filme.nome, filme.ano, filme.nota])
    
    return output.getvalue()

def exportar_json():
    filmes = Filme.select()
    dados = []
    
    for filme in filmes:
        dados.append({
            'id': filme.id,
            'nome': filme.nome,
            'ano': filme.ano,
            'nota': filme.nota
        })
    
    return json.dumps(dados, indent=2, ensure_ascii=False)

# No Streamlit
import streamlit as st

csv_data = exportar_csv()
st.download_button(
    label="📥 Baixar CSV",
    data=csv_data,
    file_name="filmes.csv",
    mime="text/csv"
)
```

---

### Exercício 15: Sistema de Avaliações

**Objetivo:** Adicionar sistema para múltiplos usuários avaliarem filmes.

**Instruções:**

1. Crie modelo `Usuario`
2. Crie modelo `Avaliacao` relacionando Usuario + Filme
3. Implemente média ponderada de avaliações
4. Mostre quem avaliou cada filme

**Solução:**

```python
# Em models.py
class Usuario(Model):
    id = AutoField(primary_key=True)
    nome = CharField(null=False, unique=True)
    
    class Meta:
        database = db
        table_name = 'usuarios'

class Avaliacao(Model):
    id = AutoField(primary_key=True)
    usuario = ForeignKeyField(Usuario, backref='avaliacoes')
    filme = ForeignKeyField(Filme, backref='avaliacoes')
    nota = FloatField(null=False)
    comentario = TextField(null=True)
    
    class Meta:
        database = db
        table_name = 'avaliacoes'

# Calcular média de avaliações
def media_avaliacoes(filme_id):
    filme = Filme.get_by_id(filme_id)
    media = (Avaliacao
             .select(fn.AVG(Avaliacao.nota))
             .where(Avaliacao.filme == filme)
             .scalar())
    return round(media, 2) if media else 0

# Listar avaliações de um filme
def listar_avaliacoes_filme(filme_id):
    filme = Filme.get_by_id(filme_id)
    return list(filme.avaliacoes)
```

---

## 🎓 Projeto Final: Sistema Completo de Biblioteca

**Objetivo:** Criar sistema completo de gerenciamento de biblioteca de filmes.

**Requisitos:**

### Modelos

1. **Filme** - id, nome, ano, duracao, sinopse, poster_url
2. **Diretor** - id, nome, nacionalidade, data_nascimento
3. **Ator** - id, nome, nacionalidade, data_nascimento
4. **Genero** - id, nome
5. **FilmeGenero** - tabela intermediária (N:M)
6. **FilmeAtor** - tabela intermediária (N:M) com campo "personagem"
7. **Usuario** - id, nome, email
8. **Avaliacao** - id, usuario, filme, nota, comentario, data

### Funcionalidades

1. **CRUD completo** para todos os modelos
2. **Busca avançada** - por nome, diretor, ator, gênero, ano
3. **Filtros combinados** - múltiplos critérios simultaneamente
4. **Estatísticas**:
   - Top 10 filmes
   - Filmes por gênero
   - Filmes por década
   - Diretores mais prolíficos
   - Atores com mais filmes
5. **Sistema de avaliação**:
   - Usuários podem avaliar filmes
   - Média de avaliações
   - Listagem de comentários
6. **Exportação**:
   - CSV
   - JSON
   - Relatório em PDF (bonus)
7. **Interface Streamlit**:
   - Sidebar com navegação
   - Múltiplas páginas
   - Gráficos interativos
   - Filtros dinâmicos

### Critérios de Avaliação

- **Funcionalidade** (40%): Todas as features funcionando
- **Código** (30%): Organização, comentários, boas práticas
- **Interface** (20%): Usabilidade, design, UX
- **Criatividade** (10%): Features extras, inovação

---

**🎉 Boa sorte com os exercícios!**

**Dica:** Comece pelos básicos e vá progredindo. Teste cada funcionalidade antes de avançar!
