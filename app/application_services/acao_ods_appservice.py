from app.services.acao_ods_service import AcaoOdsService
from app.services.acoes_service import AcaoService
from app.services.sdg_mapper_service import SDGMapperService

from sqlalchemy.orm import Session

from app.schemas.acao import AcaoCreate

class AcaoOdsAppService:

    def __init__(
        self,
        db: Session,
        acao_ods_service = AcaoOdsService,
        acao_service = AcaoService,
        sdg_mapper_service = SDGMapperService
    ):
        self.db = db
        self.acao_ods_service = acao_ods_service(db)
        self.acao_service = acao_service(db)
        self.sdg_mapper_service = sdg_mapper_service(db)

    def criar_acao_com_ods(self, acao_data: AcaoCreate):
        ods_ids = self.sdg_mapper_service.map_ods_to_ids(acao_data)

        acao_criada = self.acao_service.criar_acao(acao_data)

        self.acao_ods_service.create_bulk(acao_criada.id, ods_ids)

        return acao_criada