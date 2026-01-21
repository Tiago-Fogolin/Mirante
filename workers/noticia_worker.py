from app.models.noticia import Noticia
from app.database import SessionLocal
from app.services.sdg_mapper_service import SDGMapperService

def check_and_add_noticia(dados_noticia: Noticia):
    db = SessionLocal()
    sdg_mapper = SDGMapperService(db)
    sdg_request = sdg_mapper.make_request(dados_noticia.conteudo_integral)

    ods_encontradas = sdg_mapper.get_ods_from_raw_request(sdg_request)

    if ods_encontradas:
        print("Alguma ods encontrada... Salvando noticia")
        db.add(dados_noticia)
        db.commit()
    else:
        print("Nenhuma ods encontrada, pulando noticia")
