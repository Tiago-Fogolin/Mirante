from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table
from app.database import Base
from sqlalchemy.orm import relationship

noticia_ods_association = Table(
    'noticia_ods',
    Base.metadata,
    Column('acao_id', Integer, ForeignKey('noticias.id'), primary_key=True),
    Column('tema_id', Integer, ForeignKey('ods.id'), primary_key=True)
)

class Noticia(Base):
    __tablename__ = "noticias"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, unique=True)
    data_publicacao = Column(Date)
    url_completa = Column(String)
    conteudo_integral = Column(String)
    url_imagem = Column(String)

    municipio_id = Column(Integer, ForeignKey("municipios.id"), nullable=False)

    municipio = relationship("Municipio", back_populates="noticias")
    ods = relationship(
        "ODS",
        secondary=noticia_ods_association,
        back_populates="noticias"
    )
