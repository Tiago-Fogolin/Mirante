from crawler.noticia_crawler.noticias_crawler import *
import requests
from bs4 import BeautifulSoup
from datetime import date
from urllib.parse import urlparse

mapa_meses = {
    'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
    'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12
}

class NoticiasRibeiraoPretoCrawler():
    def __init__(self, base_url):
        self.base_url = base_url
        self.municipio_id = buscar_municipio_id("Ribeirão Preto")
        dominio = urlparse(base_url)
        self.dominio = f"{dominio.scheme}://{dominio.netloc}"

    def buscar_conteudo(self, url) -> BeautifulSoup:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def buscar_noticias(self, dia_de, dia_ate) -> BeautifulSoup:
        data_lista = dia_de.split('-')
        dia = data_lista[0]
        mes = data_lista[1]
        ano = data_lista[2]

        url = self.base_url + f"todas-noticias?ultimas=false&strFiltroData={ano}{mes}{dia}&periodoBusca=dt&status=noticia"
        return self.buscar_conteudo(url)

    def extrair_url_noticias(self, dia_de, dia_ate) -> List[str]:
        retorno = []

        total_paginas = 1

        pagina_atual = 1
        while pagina_atual <= total_paginas:
            conteudo = self.buscar_noticias(dia_de, dia_ate)

            if pagina_atual == 1:
                paginacao = conteudo.find("span", class_="ui-paginator-current")
                if paginacao:
                    texto_paginacao_dividido = paginacao.text.split()
                    if (texto_paginacao_dividido[-1]).isnumeric():
                        total_paginas = int(texto_paginacao_dividido[-1])

            ref_noticias = conteudo.find("tbody", class_="ui-datatable-data ui-widget-content").find_all("tr")

            for item in ref_noticias:
                td = item.find("td")
                link_tag = td.find("a") if td else None
                if not link_tag:
                    continue
                retorno.append(link_tag["href"])

            pagina_atual += 1

        return retorno

    def extrair_noticias(self, url_noticias) -> List[NoticiaExtraida]:
        resultado = []
        for url in url_noticias:
            conteudo = self.buscar_conteudo(self.base_url + url).find("div", class_="noticia-card-wrapper")

            titulo_div = conteudo.find("h1", class_="noticia-titulo")
            titulo = ""
            if titulo_div:
                titulo = titulo_div.text

            data_div = conteudo.find("div", class_="noticia-meta")
            data_formatada = None
            if data_div:
                data_texto = data_div.text.strip().split(" às")[0].strip()
                partes = data_texto.split("/")
                dia = int(partes[0])
                mes = int(partes[1])
                ano = int(partes[2])

                data_formatada = date(ano, mes, dia)

            corpo_div = conteudo.find("div", class_="noticia-corpo")
            conteudo_integral = ""
            url_imagem = ""
            if corpo_div:
                for paragrafo in corpo_div.find_all("p"):
                    span = paragrafo.find("span")
                    if span:
                        conteudo_integral += f"{span.text}\n"

                img = corpo_div.find("img")
                if img:
                    url_imagem = self.dominio + img["src"]

            noticia_extraida = NoticiaExtraida(
                url_completa=self.base_url + url,
                data_publicacao=data_formatada,
                titulo=titulo,
                conteudo_integral=conteudo_integral,
                url_imagem=url_imagem,
                municipio_id=self.municipio_id
            )

            resultado.append(noticia_extraida)

        return resultado

    def rodar_crawler(self, dia_de: str, dia_ate: str):

        urls = self.extrair_url_noticias(dia_de, dia_ate)
        noticias = self.extrair_noticias(urls)

        return noticias
