from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models.acao import StatusAcaoEnum
from app.schemas.municipio import Municipio

class AcaoBase(BaseModel):
    titulo: str
    tema: str
    descricao: str
    data_inicio: date
    status: Optional[StatusAcaoEnum] = StatusAcaoEnum.NAO_INICIADA
    municipio_id: int


class AcaoCreate(AcaoBase):
    pass

class Acao(AcaoBase):
    id: int
    municipio: Municipio

    class Config:
        orm_mode = True