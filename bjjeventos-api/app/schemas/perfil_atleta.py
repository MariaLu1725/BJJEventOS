from pydantic import BaseModel
from datetime import date

class PerfilAtletaBase(BaseModel):
    data_nascimento: date
    genero: str
    faixa: str
    peso_atual_kg: float
    academia_equipe: str

class PerfilAtletaCreate(PerfilAtletaBase):
    pass

class PerfilAtletaResponse(PerfilAtletaBase):
    id: int
    usuario_id: int
    faixa_confirmada: bool

    class Config:
        from_attributes = True
