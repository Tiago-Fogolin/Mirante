from pydantic import BaseModel
from app.schemas.municipio import Municipio
from datetime import date

class NoticiaBase(BaseModel):
    titulo: str
    data_publicacao: date
    url_completa: str
    conteudo_integral: str
    url_imagem: str


class Noticia(NoticiaBase):
    id: int
    municipio: Municipio

    class Config:
        orm_mode = True
