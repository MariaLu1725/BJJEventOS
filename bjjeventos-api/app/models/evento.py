from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Evento(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(String(500), nullable=True)
    local_ginasio = Column(String(150), nullable=False)
    data_evento = Column(DateTime, nullable=False)
    data_limite_inscricao = Column(DateTime, nullable=False)
    data_checagem_geral = Column(DateTime, nullable=False)
    qtd_tatames = Column(Integer, default=4)
    organizador_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    organizador = relationship("Usuario", back_populates="eventos")
    categorias = relationship("Categoria", back_populates="evento")
