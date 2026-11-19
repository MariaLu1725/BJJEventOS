from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.inscricao import Inscricao
from app.schemas.inscricao import InscricaoCreate, InscricaoResponse
from app.core.deps import get_current_user, require_roles

router = APIRouter(prefix="/inscricoes", tags=["Inscrições"])

@router.post("", response_model=InscricaoResponse, status_code=status.HTTP_201_CREATED)
def realizar_inscricao(
    insc_in: InscricaoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(require_roles(["atleta"]))
):
    if not current_user.perfil_atleta:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você precisa preencher sua ficha de atleta primeiro.")

    categoria = db.query(Categoria).filter(Categoria.id == insc_in.categoria_id).first()
    if not categoria:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria não encontrada.")

    if categoria.peso_limite_kg and current_user.perfil_atleta.peso_atual_kg > categoria.peso_limite_kg:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Seu peso atual excede o limite permitido desta categoria.")

    ja_inscrito = db.query(Inscricao).filter(
        Inscricao.atleta_id == current_user.id,
        Inscricao.categoria_id == insc_in.categoria_id
    ).first()
    if ja_inscrito:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Você já está inscrito nesta categoria.")

    nova_insc = Inscricao(
        atleta_id=current_user.id,
        categoria_id=insc_in.categoria_id,
        status_pagamento="Pago",
        status_pesagem="Aguardando"
    )
    db.add(nova_insc)
    db.commit()
    db.refresh(nova_insc)
    return nova_insc
