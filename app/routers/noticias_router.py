from app.services.noticias_service import NoticiasService
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.dependencies import get_db
from app.schemas.noticia import Noticia
from typing import Optional

router = APIRouter(prefix="/noticias", tags=["noticias"])


@router.get("/", response_model=list[Noticia])
def get_noticias(municipio_id: Optional[int] = None,db: Session = Depends(get_db)):
    noticias_service = NoticiasService(db)
    return noticias_service.get_all(municipio_id=municipio_id)
