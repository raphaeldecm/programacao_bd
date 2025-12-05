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
