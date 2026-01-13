from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Text, Boolean
from app.database import Base
from sqlalchemy.orm import relationship
from app.models.tema import acao_temas_association
import enum
from sqlalchemy.ext.associationproxy import association_proxy


class StatusAcaoEnum(enum.Enum):
    NAO_INICIADA = 0
    EM_ANDAMENTO = 1
    FINALIZADA   = 2

class Acao(Base):
    __tablename__ = "acoes"
    id = Column(Integer, primary_key=True, index=True)

    # primeiro quadro
    nome_organizacao = Column(String, index=True)
    sigla_organizacao = Column(String)
    documento_ator = Column(String)
    tipo_ator = Column(String)
    ano_fundacao = Column(Integer)
    municipio_id = Column(Integer, ForeignKey("municipios.id"), nullable=False)
    endereco_completo = Column(String)
    regiao_administrativa = Column(String)
    website = Column(String)
    email_contato = Column(String)
    telefone_contato = Column(String)
    redes_sociais = Column(String)
    abrangencia_geografica = Column(String)

    # segundo quadro
    temas = relationship(
        "Tema",
        secondary=acao_temas_association,
        back_populates="acoes"
    )

    # terceiro quadro
    status = Column(Enum(StatusAcaoEnum), nullable=False, default=StatusAcaoEnum.NAO_INICIADA)
    titulo = Column(String, nullable=False, index=True)
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)
    descricao = Column(Text, nullable=False)
    publico_alvo = Column(String)
    numero_colaboradores = Column(Integer)
    financiador = Column(String)
    valor_financiamento = Column(String)
    objetivos = Column(String)
    resultados_esperados = Column(Text)
    resultados_alcancados = Column(Text)
    aprendizados_inovacoes = Column(Text)

    # quarto quadro
    parcerias_envolvidas = Column(Text)
    tipo_parceria = Column(String)
    periodo_parceria = Column(String) # talvez data inicio e data fim?
    area_cooperacao = Column(String)

    possui_vinculo = Column(Boolean, default=False)
    vinculo_politica_publica = Column(String)

    participa_conselhos = Column(Boolean, default=False)
    participacao_conselhos = Column(String)

    usa_dados_abertos = Column(Boolean, default=False)
    links_relatorios = Column(Text)
    exemplo_uso_dados = Column(Text)


    # quinto quadro
    tecnologias_utilizadas = Column(Text)
    indicadores_impacto = Column(Text)
    premios_recebidos = Column(Text)
    observacoes = Column(Text)

    municipio = relationship("Municipio", back_populates="acoes")
    acao_ods = relationship("AcaoOds", back_populates="acao", cascade="all, delete-orphan")
    ods = association_proxy("acao_ods", "ods")
