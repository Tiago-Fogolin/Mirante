from pydantic import BaseModel, EmailStr
from app.models.usuario import TipoPerfilEnum
from app.schemas.municipio import Municipio

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    tipo_perfil: TipoPerfilEnum
    municipio_id: int


class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int
    municipio: Municipio
    class Config:
        orm_mode = True
