from sqlalchemy import Column, Integer, String, Date
from app.database import Base
from sqlalchemy.orm import relationship


class Noticia(Base):
    __tablename__ = "noticias"
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, unique=True, index=True)
    data_publicacao = Column(Date, index=True)
    url_completa = Column(String, index=True)
    conteudo_integral = Column(String, index=True)
    url_imagem = Column(String, index=True)
