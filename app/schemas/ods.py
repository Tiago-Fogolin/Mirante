from pydantic import BaseModel
from typing import Optional

class ODSBase(BaseModel):
    numero: int
    nome: Optional[str] = None

class ODSCreate(ODSBase):
    pass

class ODS(ODSBase):
    id: int

    class Config:
        orm_mode = True
