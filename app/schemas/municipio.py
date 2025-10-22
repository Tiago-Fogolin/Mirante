from pydantic import BaseModel, field_validator

class MunicipioBase(BaseModel):
    nome: str
    uf: str
    geojson_limite: str | None = None

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