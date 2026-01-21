from app.services.acao_ods_service import AcaoOdsService
from app.services.sdg_mapper_service import SDGMapperService
from app.database import SessionLocal

def save_sdgmapper_ods(acao_criada):
    db = SessionLocal()
    acao_ods_service = AcaoOdsService(db)
    sdg_mapper_service = SDGMapperService(db)
    ods_ids = sdg_mapper_service.map_ods_to_ids(acao_criada)
    acao_ods_service.create_bulk(acao_criada.id, ods_ids)

    print(f"Sucesso! ODS encontradas: {ods_ids}")
