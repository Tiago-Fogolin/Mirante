
from app.models.ods import ODS
from sqlalchemy.orm import Session
from app.schemas.acao import AcaoCreate
from app.models.acao import StatusAcaoEnum
import requests
from dotenv import load_dotenv
import os
import json

# TODO -> adicionar tratamento de erro com a comunicação do sdg mapper

load_dotenv()

from typing import List

API_KEY = os.getenv("SDG_MAPPER_KEY")

class SDGMapperService:

    def __init__(self, db: Session):
        self.db = db
        self.url = "https://knowsdgs.jrc.ec.europa.eu/api/rest/mappingdata"

    def sanitize_data(self, dados: AcaoCreate) -> str:
        partes_texto = []

        if dados.nome_organizacao:
            texto_org = f"Sobre a Organização:\n{dados.nome_organizacao}"

            if dados.tipo_ator:
                texto_org += f" é um ator do tipo {dados.tipo_ator}."

            if dados.website:
                texto_org += f" (Site: {dados.website})"

            partes_texto.append(texto_org)

        status_desc = {
            StatusAcaoEnum.EM_ANDAMENTO: "está atualmente em execução",
            StatusAcaoEnum.FINALIZADA: "foi finalizada"
        }.get(dados.status, "é uma iniciativa")

        bloco_acao = (
            f"Sobre a Iniciativa:\n"
            f"O projeto '{dados.titulo}' {status_desc}. "
            f"Descrição principal: {dados.descricao}."
        )

        if dados.abrangencia_geografica:
            bloco_acao += f" A abrangência geográfica da ação foca em: {dados.abrangencia_geografica}."

        partes_texto.append(bloco_acao)

        texto_impacto = "Impacto e Resultados:\n"
        tem_impacto = False

        if dados.resultados_esperados:
            texto_impacto += f"Os resultados esperados são: {dados.resultados_esperados}. "
            tem_impacto = True

        if dados.resultados_alcancados:
            texto_impacto += f"Até o momento, os resultados alcançados foram: {dados.resultados_alcancados}. "
            tem_impacto = True

        if dados.indicadores_impacto:
            texto_impacto += f"O monitoramento é feito através dos indicadores: {dados.indicadores_impacto}."
            tem_impacto = True

        if tem_impacto:
            partes_texto.append(texto_impacto)

        if dados.aprendizados_inovacoes or dados.tecnologias_utilizadas:
            texto_inovacao = "Inovação e Aprendizado:\n"

            if dados.tecnologias_utilizadas:
                texto_inovacao += f"Tecnologias utilizadas: {dados.tecnologias_utilizadas}. "

            if dados.aprendizados_inovacoes:
                texto_inovacao += f"Aprendizados e inovações geradas: {dados.aprendizados_inovacoes}."

            partes_texto.append(texto_inovacao)

        politicas = dados.vinculo_politica_publica
        conselhos = dados.participacao_conselhos
        parcerias = dados.parcerias_envolvidas
        financiador = dados.financiador

        if any([politicas, conselhos, parcerias, financiador]):
            bloco_contexto = "Ecossistema e Parcerias:\n"

            if politicas:
                bloco_contexto += f"A ação possui vínculo com a política pública: {politicas}. "

            if conselhos:
                bloco_contexto += f"Participa dos conselhos: {conselhos}. "

            if parcerias:
                bloco_contexto += f"Conta com as parcerias de: {parcerias}. "

            if financiador:
                bloco_contexto += f"Financiado por: {financiador}."

            partes_texto.append(bloco_contexto)

        texto_final = "\n\n".join(partes_texto)


        return texto_final

    def map_ods_to_ids(self, acao_data: AcaoCreate) -> List[int]:
        sdg_results = self.make_request(self.sanitize_data(acao_data))
        ods_numeros = self.get_ods_from_raw_request(sdg_results)

        ods_in_db = self.db.query(ODS).filter(ODS.numero.in_(ods_numeros)).all()

        ods_ids = [ods.id for ods in ods_in_db]
        return ods_ids

    def get_ods_from_raw_request(self, raw_request):
        data = json.loads(json.loads(raw_request.text)["data"][0])
        children = data.get("children", [])
        retorno = []
        for child in children:
            if child.get("name", None):
                retorno.append(child["name"].split()[-1])

        return retorno

    def make_request(self, data):
        headers = {"Content-Type": "application/json", "X-Api-Key": API_KEY}
        response = requests.post(
            self.url,
            headers=headers,
            json={"input_text": data, "source_language": "pt"}
        )

        return response
