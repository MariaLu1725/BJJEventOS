from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.schemas.perfil_atleta import PerfilAtletaResponse

class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    perfil: str

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    perfil: str
    criado_em: datetime
    perfil_atleta: Optional[PerfilAtletaResponse] = None

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
    perfil: str
    usuario_id: int
