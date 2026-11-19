from pydantic import BaseModel
from typing import Optional

class ResultadoLutaUpdate(BaseModel):
    vencedor_id: int
    metodo_vitoria: str
    placar_detalhado: str

class LutaResponse(BaseModel):
    id: int
    categoria_id: int
    fase: str
    tatame_numero: int
    ordem_luta: int
    atleta_1_id: int
    atleta_2_id: int
    vencedor_id: Optional[int] = None
    metodo_vitoria: Optional[str] = None
    placar_detalhado: Optional[str] = None

    class Config:
        from_attributes = True
