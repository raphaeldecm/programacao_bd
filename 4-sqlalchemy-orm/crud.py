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
