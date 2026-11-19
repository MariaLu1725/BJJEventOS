from pydantic import BaseModel
from typing import Optional

class CategoriaCreate(BaseModel):
    modalidade: str
    genero: str
    divisao_idade: str
    faixa: str
    nome_categoria: str
    peso_limite_kg: Optional[float] = None

class CategoriaResponse(CategoriaCreate):
    id: int
    evento_id: int

    class Config:
        from_attributes = True
