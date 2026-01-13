from sqlalchemy.orm import Session
from app.models.acao import Acao as AcaoModel
from app.models.tema import Tema as TemaModel
from app.schemas.acao import AcaoCreate

class AcaoService:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(AcaoModel).all()

    def get_count(self):
        return self.db.query(AcaoModel).count()

    def get_by_id(self, id):
        return self.db.query(AcaoModel).get(id)

    def criar_acao(self, data: AcaoCreate):
        dados_acao = data.model_dump()

        temas_ids = dados_acao.pop("temas_ids", [])

        # remove o campo de ods, ja populado
        dados_acao.pop("ods_ids")

        db_acao = AcaoModel(**dados_acao)

        if temas_ids:
            temas_objetos = self.db.query(TemaModel).filter(TemaModel.id.in_(temas_ids)).all()

            db_acao.temas = temas_objetos

        self.db.add(db_acao)
        self.db.commit()
        self.db.refresh(db_acao)

        return db_acao
