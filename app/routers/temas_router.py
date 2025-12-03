from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tema import Tema, TemaCreate
from app.schemas.usuario import Usuario
from app.dependencies import get_db
from app.core.deps import get_current_user
from app.services.temas_service import TemaService

router = APIRouter(prefix="/temas", tags=["temas"])

@router.post("/", response_model=Tema)
def criar_tema(tema: TemaCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    tema_service = TemaService(db)
    return tema_service.criar_tema(tema)


@router.get("/", response_model=list[Tema])
def listar_temas(db: Session = Depends(get_db)):
    tema_service = TemaService(db)
    return tema_service.get_all()


@router.get("/{id}", response_model=Tema)
def get_tema(id: int, db: Session = Depends(get_db)):
    tema_service = TemaService(db)
    tema = tema_service.get_by_id(id)

    if not tema:
        raise HTTPException(status_code=404, detail="Tema não encontrado")

    return tema
