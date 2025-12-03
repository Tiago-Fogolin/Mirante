from pydantic import BaseModel
from typing import Optional


class TemaBase(BaseModel):
    nome: str
    descricao: Optional[str]


class TemaCreate(TemaBase):
    pass

class Tema(TemaBase):
    id: int

    class Config:
        orm_mode = True
