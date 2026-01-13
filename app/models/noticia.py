from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.database import Base
from sqlalchemy.orm import relationship


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
