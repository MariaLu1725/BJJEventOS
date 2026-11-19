from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventoCreate(BaseModel):
    nome: str
    descricao: Optional[str] = None
    local_ginasio: str
    data_evento: datetime
    data_limite_inscricao: datetime
    data_checagem_geral: datetime
    qtd_tatames: int = 4

class EventoResponse(EventoCreate):
    id: int
    organizador_id: int

    class Config:
        from_attributes = True
