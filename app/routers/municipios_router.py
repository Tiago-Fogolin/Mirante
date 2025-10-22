from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.municipio import Municipio, MunicipioCreate
from app.schemas.usuario import Usuario
from app.dependencies import get_db
from app.core.deps import get_current_user
from app.services.municipios_service import MunicipioService

router = APIRouter(prefix="/municipios", tags=["municipios"])

@router.post("/", response_model=Municipio)
def criar_municipio(municipio: MunicipioCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    municipio_service = MunicipioService(db)
    return municipio_service.criar_municipio(municipio)


@router.get("/", response_model=list[Municipio])
def listar_municipios(db: Session = Depends(get_db)):
    municipio_service = MunicipioService(db)
    return municipio_service.get_all()


@router.get("/{id}", response_model=Municipio)
def get_municipio(id: int, db: Session = Depends(get_db)):
    municipio_service = MunicipioService(db)
    municipio = municipio_service.get_by_id(id)
    
    if not municipio:
        raise HTTPException(status_code=404, detail="Município não encontrado")

    return municipio