from pydantic import BaseModel

class ODSBase(BaseModel):
    numero: int
    nome: str

class ODSCreate(ODSBase):
    pass

class ODS(ODSBase):
    id: int

    class Config:
        orm_mode = True
    