from typing import List
from dataclasses import dataclass
from bs4 import BeautifulSoup
from datetime import date


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

@dataclass
class NoticiaExtraida:
    url_completa: str
    data_publicacao: date | None
    titulo: str
    conteudo_integral: str
    url_imagem: str
    municipio_id: int

# class CrawlerNoticias:

#     def __init__(self, base_url):
#         self.base_url = base_url

#     def buscar_conteudo(self, dia_de, dia_ate, pagina=1) -> BeautifulSoup:
#         """
#             Retorna conteúdo "raw" do site
#         """

#         raise NotImplementedError()

#     def extrair_url_noticias(self, dia_de, dia_ate) -> List[str]:
#         """
#             Extrai todas as urls que depois serão percorridas
#         """

#         raise NotImplementedError()


#     def extrair_noticias(self, url_noticias) -> List[NoticiaExtraida]:
#         """
#             Retorna a lista das noticias extraídas
#         """

#         raise NotImplementedError()


#     def rodar_crawler(self, dia_de: str, dia_ate: str) -> List[NoticiaExtraida]:
#         """
#         Orquestra todas as etapas: busca, extração e classificação.
#         """
#         raw_conteudo = self.buscar_conteudo(dia_de, dia_ate)
#         noticias_extraidas = self.extrair_noticias(raw_conteudo)
#         # TODO -> adicionar classificação de ODS aqui antes de retornar

#         return noticias_extraidas
