from pydantic import BaseModel, field_validator

class MunicipioBase(BaseModel):
    nome: str
    uf: str
    latitude: float
    longitude: float

class MunicipioCreate(MunicipioBase):

    @field_validator("uf")
    def validar_uf(cls, v):
        if len(v) != 2:
            raise ValueError("UF deve ter 2 caracteres")
        return v.upper()

class Municipio(MunicipioBase):
    id: int
    class Config:
        orm_mode = True
