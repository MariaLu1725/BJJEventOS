from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class PerfilAtleta(Base):
    __tablename__ = "perfis_atleta"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), unique=True, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    genero = Column(String(10), nullable=False)
    faixa = Column(String(20), nullable=False)
    peso_atual_kg = Column(Float, nullable=False)
    academia_equipe = Column(String(100), nullable=False)
    faixa_confirmada = Column(Boolean, default=True)

    usuario = relationship("Usuario", back_populates="perfil_atleta")
