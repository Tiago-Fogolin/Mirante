from sqlalchemy.orm import Session
from app.models.noticia import Noticia as NoticiaModel
from typing import Optional

class NoticiasService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self, municipio_id: Optional[int] = None):
        query = self.db.query(NoticiaModel)

        if municipio_id is not None:
            query = query.filter(NoticiaModel.municipio_id==municipio_id)

        return query.all()
