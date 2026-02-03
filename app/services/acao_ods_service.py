from typing import List
from sqlalchemy.orm import Session
from app.models.acao_ods import AcaoOds

class AcaoOdsService:
    def __init__(self, db: Session):
        self.db = db

    def create(self, acao_id: int, ods_id: int) -> AcaoOds:
        acao_ods = AcaoOds(acao_id=acao_id, ods_id=ods_id)

        self.db.add(acao_ods)
        self.db.commit()
        self.db.refresh(acao_ods)

        return acao_ods

    def create_bulk(self, acao_id: int, ods_ids: List[int]) -> List[AcaoOds]:
        existing_ids = (
                self.db.query(AcaoOds.ods_id)
                .filter(AcaoOds.acao_id == acao_id)
                .filter(AcaoOds.ods_id.in_(ods_ids))
                .all()
            )
        existing_ids_list = [item[0] for item in existing_ids]

        new_items = [
            AcaoOds(acao_id=acao_id, ods_id=ods_id)
            for ods_id in ods_ids if ods_id not in existing_ids_list
        ]

        if new_items:
            self.db.add_all(new_items)
            self.db.commit()

        return new_items
