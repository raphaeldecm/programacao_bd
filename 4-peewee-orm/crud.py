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
