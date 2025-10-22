from pydantic import BaseModel, EmailStr
from app.models.usuario import TipoPerfilEnum

class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    tipo_perfil: TipoPerfilEnum
    municipio_id: int


class UsuarioCreate(UsuarioBase):
    senha: str

class Usuario(UsuarioBase):
    id: int

    class Config:
        orm_mode = True
