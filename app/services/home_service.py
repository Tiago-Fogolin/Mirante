from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.municipio import Municipio as MunicipioModel
from app.models.acao import Acao as AcaoModel
from app.services.acoes_service import AcaoService
from app.services.municipios_service import MunicipioService
from app.services.ods_service import ODSService

class HomeService:
    
    def __init__(
            self, 
            db: Session,
            municipios_service = MunicipioService,
            acoes_service = AcaoService,
            ods_service = ODSService
        ):

        self.db = db

        self.municipios_service = municipios_service(db)
        self.acoes_service = acoes_service(db)
        self.ods_service = ods_service(db)

    def top_municipios_por_acoes(self, limite: int = 3):
        resultados = (
            self.db.query(
                MunicipioModel.id,
                MunicipioModel.nome,
                func.count(AcaoModel.id).label("total_acoes")
            )
            .join(AcaoModel)
            .group_by(MunicipioModel.id)
            .limit(limite)
            .all()
        )

        retorno = [
            {
                "id": r.id,
                "nome": r.nome,
                "total_acoes": r.total_acoes
            }
            for r in resultados
        ]

        return retorno
    
    # TODO -> adicionar esse relacionamento
    # ainda não tem tabela de ods -> acao
    # def top_acoes_por_ods(self, limite: int =3):
    #     return (
    #         self.db.query(
    #             ODSModel.id,
    #             ODSModel.nome
    #         )
    #     )

    def get_home_data(self):
        qtd_municipios = self.municipios_service.get_count()
        qtd_acoes = self.acoes_service.get_count()
        qtd_ods = self.ods_service.get_count()
        top_municipios = self.top_municipios_por_acoes()

        return {
            "qtd_municipios": qtd_municipios,
            "qtd_acoes": qtd_acoes,
            "qtd_ods": qtd_ods,
            "top_municipios": top_municipios,
            "ods_em_alta": [],
            "ultimas_noticias": []
        }