from pydantic import BaseModel
from datetime import datetime

class InscricaoCreate(BaseModel):
    categoria_id: int

class InscricaoResponse(BaseModel):
    id: int
    atleta_id: int
    categoria_id: int
    status_pagamento: str
    status_pesagem: str
    data_inscricao: datetime

    class Config:
        from_attributes = True
