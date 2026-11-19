from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from app.database import Base

class Inscricao(Base):
    __tablename__ = "inscricoes"

    id = Column(Integer, primary_key=True, index=True)
    atleta_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    status_pagamento = Column(String(20), default="Pendente")
    status_pesagem = Column(String(20), default="Aguardando")
    data_inscricao = Column(DateTime, default=lambda: datetime.now(timezone.utc))

    atleta = relationship("Usuario", back_populates="inscricoes")
    categoria = relationship("Categoria", back_populates="inscricoes")
