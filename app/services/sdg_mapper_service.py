
from app.models.ods import ODS
from sqlalchemy.orm import Session
from app.schemas.acao import AcaoCreate

from typing import List

class SDGMapperService:

    def __init__(self, db: Session):
        self.db = db

    def map_ods_to_ids(self, acao_data: AcaoCreate) -> List[int]:        
        sdg_results = self.make_request(acao_data)

        ods_numeros = [item["numero"] for item in sdg_results]
        ods_in_db = self.db.query(ODS).filter(ODS.numero.in_(ods_numeros)).all()

        ods_ids = [ods.id for ods in ods_in_db]
        return ods_ids

    def make_request(self, acao_data):
        response = []
        
        return response