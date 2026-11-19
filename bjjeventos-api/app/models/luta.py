from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Luta(Base):
    __tablename__ = "lutas"

    id = Column(Integer, primary_key=True, index=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    fase = Column(String(30), nullable=False)
    tatame_numero = Column(Integer, nullable=False)
    ordem_luta = Column(Integer, nullable=False)
    atleta_1_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    atleta_2_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    vencedor_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    metodo_vitoria = Column(String(40), nullable=True)
    placar_detalhado = Column(String(50), nullable=True)

    categoria = relationship("Categoria", back_populates="lutas")
