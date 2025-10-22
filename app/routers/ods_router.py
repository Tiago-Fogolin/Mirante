from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.ods import ODS, ODSCreate
from app.schemas.usuario import Usuario
from app.dependencies import get_db
from app.core.deps import get_current_user
from app.services.ods_service import ODSService

router = APIRouter(prefix="/ods", tags=["ods"])

@router.post("/", response_model=ODS)
def criar_ods(acao: ODSCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    acao_service = ODSService(db)
    return acao_service.criar_ods(acao)


@router.get("/", response_model=list[ODS])
def listar_ods(db: Session = Depends(get_db)):
    acao_service = ODSService(db)
    return acao_service.get_all()
