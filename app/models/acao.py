from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Text, Boolean
from app.database import Base
from sqlalchemy.orm import relationship
import enum


class StatusAcaoEnum(enum.Enum):
    NAO_INICIADA = 0
    EM_ANDAMENTO = 1
    FINALIZADA   = 2

class Acao(Base):
    __tablename__ = "acoes"

    # --- Identificadores ---
    id = Column(Integer, primary_key=True, index=True)
    municipio_id = Column(Integer, ForeignKey("municipios.id"), nullable=False)

    # --- Dados Básicos do Projeto (Vêm do Excel "Nome do projeto", "Temas", etc) ---
    titulo = Column(String, nullable=False, index=True)
    tema = Column(String, nullable=False)
    descricao = Column(Text, nullable=False)
    status = Column(Enum(StatusAcaoEnum), nullable=False, default=StatusAcaoEnum.NAO_INICIADA)

    # --- Prazos ---
    data_inicio = Column(Date, nullable=True)
    data_fim = Column(Date, nullable=True)

    # --- Dados da Organização/Ator (Extraídos das colunas de "Ator") ---
    # Nota: Idealmente, no futuro, isso viraria uma tabela "Organizacoes" separada
    nome_organizacao = Column(String, index=True)
    sigla_organizacao = Column(String)
    documento_ator = Column(String)
    tipo_ator = Column(String)
    ano_fundacao = Column(Integer)

    # --- Localização e Contato da Organização ---
    endereco_completo = Column(String)
    regiao_administrativa = Column(String)
    website = Column(String)
    email_contato = Column(String)
    telefone_contato = Column(String)
    redes_sociais = Column(String)

    # --- Detalhes da Execução e Impacto ---
    abrangencia_geografica = Column(String)

    # Resultados (Criei campos separados para 'esperados' e 'alcançados' conforme o Excel)
    resultados_esperados = Column(Text)
    resultados_alcancados = Column(Text)
    aprendizados_inovacoes = Column(Text)

    # Parcerias e Financiamento
    parcerias_envolvidas = Column(Text)
    tipo_parceria = Column(String)
    financiador = Column(String)
    valor_financiamento = Column(String)

    # --- Dados Estratégicos e Políticas Públicas ---
    vinculo_politica_publica = Column(String)
    participacao_conselhos = Column(String)

    # --- Tecnologia e Dados ---
    usa_dados_abertos = Column(Boolean, default=False)
    exemplo_uso_dados = Column(Text)
    tecnologias_utilizadas = Column(Text)
    links_relatorios = Column(Text)

    # --- Outros ---
    indicadores_impacto = Column(Text)
    premios_recebidos = Column(Text)
    observacoes = Column(Text)
    numero_colaboradores = Column(Integer)

    # --- Relacionamentos ---
    municipio = relationship("Municipio", back_populates="acoes")
    acao_ods = relationship("AcaoOds", back_populates="acao", cascade="all, delete-orphan")
