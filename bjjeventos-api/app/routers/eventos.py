from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.models.evento import Evento
from app.schemas.evento import EventoCreate, EventoResponse
from app.core.deps import get_current_user, require_roles

router = APIRouter(prefix="/eventos", tags=["Campeonatos"])

@router.get("", response_model=List[EventoResponse])
def listar_eventos(db: Session = Depends(get_db)):
    return db.query(Evento).all()

@router.post("", response_model=EventoResponse, status_code=status.HTTP_201_CREATED)
def criar_evento(
    evento_in: EventoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(require_roles(["organizador", "admin"]))
):
    novo_evento = Evento(
        nome=evento_in.nome,
        descricao=evento_in.descricao,
        local_ginasio=evento_in.local_ginasio,
        data_evento=evento_in.data_evento,
        data_limite_inscricao=evento_in.data_limite_inscricao,
        data_checagem_geral=evento_in.data_checagem_geral,
        qtd_tatames=evento_in.qtd_tatames,
        organizador_id=current_user.id
    )
    db.add(novo_evento)
    db.commit()
    db.refresh(novo_evento)
    return novo_evento
