from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.evento import Evento
from app.schemas.categoria import CategoriaCreate, CategoriaResponse
from app.core.deps import get_current_user, require_roles

router = APIRouter(prefix="/eventos", tags=["Categorias"])

@router.get("/{evento_id}/categorias", response_model=List[CategoriaResponse])
def listar_categorias_do_evento(evento_id: int, db: Session = Depends(get_db)):
    return db.query(Categoria).filter(Categoria.evento_id == evento_id).all()

@router.post("/{evento_id}/categorias", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def criar_categoria(
    evento_id: int,
    cat_in: CategoriaCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(require_roles(["organizador", "admin"]))
):
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Campeonato não encontrado.")

    nova_cat = Categoria(
        evento_id=evento_id,
        modalidade=cat_in.modalidade,
        genero=cat_in.genero,
        divisao_idade=cat_in.divisao_idade,
        faixa=cat_in.faixa,
        nome_categoria=cat_in.nome_categoria,
        peso_limite_kg=cat_in.peso_limite_kg
    )
    db.add(nova_cat)
    db.commit()
    db.refresh(nova_cat)
    return nova_cat
