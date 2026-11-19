from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    evento_id = Column(Integer, ForeignKey("eventos.id"), nullable=False)
    modalidade = Column(String(10), nullable=False)
    genero = Column(String(10), nullable=False)
    divisao_idade = Column(String(30), nullable=False)
    faixa = Column(String(20), nullable=False)
    nome_categoria = Column(String(30), nullable=False)
    peso_limite_kg = Column(Float, nullable=True)

    evento = relationship("Evento", back_populates="categorias")
    inscricoes = relationship("Inscricao", back_populates="categoria")
    lutas = relationship("Luta", back_populates="categoria")
