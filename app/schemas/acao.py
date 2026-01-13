from pydantic import BaseModel
from typing import Optional
from datetime import date
from app.models.acao import StatusAcaoEnum
from app.schemas.municipio import Municipio
from app.schemas.ods import ODSBase
from app.schemas.tema import Tema
from typing import List

class AcaoBase(BaseModel):
    # --- primeiro quadro ---
    nome_organizacao: str
    sigla_organizacao: Optional[str] = None
    documento_ator: Optional[str] = None
    tipo_ator: Optional[str] = None
    ano_fundacao: Optional[int] = None
    endereco_completo: Optional[str] = None
    regiao_administrativa: Optional[str] = None
    website: Optional[str] = None
    email_contato: Optional[str] = None
    telefone_contato: Optional[str] = None
    redes_sociais: Optional[str] = None
    abrangencia_geografica: Optional[str] = None

    # --- terceiro quadro ---
    status: StatusAcaoEnum = StatusAcaoEnum.NAO_INICIADA
    titulo: str
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    descricao: str
    publico_alvo: Optional[str] = None
    numero_colaboradores: Optional[int] = None
    financiador: Optional[str] = None
    valor_financiamento: Optional[str] = None
    objetivos: Optional[str] = None
    resultados_esperados: Optional[str] = None
    resultados_alcancados: Optional[str] = None
    aprendizados_inovacoes: Optional[str] = None

    # --- quarto quadro ---
    parcerias_envolvidas: Optional[str] = None
    tipo_parceria: Optional[str] = None
    periodo_parceria: Optional[str] = None
    area_cooperacao: Optional[str] = None

    possui_vinculo: bool = False
    vinculo_politica_publica: Optional[str] = None

    participa_conselhos: bool = False
    participacao_conselhos: Optional[str] = None

    usa_dados_abertos: bool = False
    links_relatorios: Optional[str] = None
    exemplo_uso_dados: Optional[str] = None

    tecnologias_utilizadas: Optional[str] = None
    indicadores_impacto: Optional[str] = None
    premios_recebidos: Optional[str] = None
    observacoes: Optional[str] = None


class AcaoCreate(AcaoBase):
    municipio_id: int
    temas_ids: List[int] = []
    # esse campo do json vem do forms, dps que ele vai ser complementado pelo sdg
    ods_ids: List[int] = []

class Acao(AcaoBase):
    id: int
    municipio: Municipio
    temas: List[Tema] = []
    ods: List[ODSBase] = []

    class Config:
        orm_mode = True
