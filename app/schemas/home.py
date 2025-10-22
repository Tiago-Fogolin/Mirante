from pydantic import BaseModel

class TopMunicipio(BaseModel):
    id: int
    nome: str
    total_acoes: int

class HomeResponse(BaseModel):
    qtd_municipios: int
    qtd_acoes: int
    qtd_ods: int
    top_municipios: list[TopMunicipio]
    ods_em_alta: list
    ultimas_noticias: list
