from app.application_services import acao_ods_appservice
from app.services.acao_ods_service import AcaoOdsService
from app.services.sdg_mapper_service import SDGMapperService
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.acao import Acao, AcaoCreate
from app.schemas.usuario import Usuario
from app.dependencies import get_db
from app.core.deps import get_current_user
from app.services.acoes_service import AcaoService
from app.application_services.acao_ods_appservice import AcaoOdsAppService

router = APIRouter(prefix="/acoes", tags=["acoes"])

@router.post("/", response_model=Acao)
def criar_acao(acao: AcaoCreate, db: Session = Depends(get_db), usuario: Usuario = Depends(get_current_user)):
    appservice = AcaoOdsAppService(db, AcaoOdsService, AcaoService)
    return appservice.criar_acao_com_ods(acao)


@router.get("/", response_model=list[Acao])
def listar_acoes(db: Session = Depends(get_db)):
    acao_service = AcaoService(db)
    return acao_service.get_all()


@router.get("/{id}", response_model=Acao)
def get_acao(id: int, db: Session = Depends(get_db)):
    acao_service = AcaoService(db)
    acao = acao_service.get_by_id(id)

    if not acao:
        raise HTTPException(status_code=404, detail="Ação não encontrada")

    return acao
