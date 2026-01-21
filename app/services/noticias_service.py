from sqlalchemy.orm import Session
from app.models.noticia import Noticia as NoticiaModel


class NoticiasService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(NoticiaModel).all()
