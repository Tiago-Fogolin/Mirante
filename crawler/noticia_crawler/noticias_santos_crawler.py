from crawler.noticia_crawler.noticias_crawler import *
import requests
from bs4 import BeautifulSoup
from datetime import date

mapa_meses = {
    'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6,
    'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12
}

class NoticiasSantosCrawler():
    def __init__(self, base_url):
        self.base_url = base_url
        self.municipio_id = 4

    def buscar_conteudo(self, url) -> BeautifulSoup:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def buscar_noticias(self) -> BeautifulSoup:
        url = self.base_url + "/?q=lista-de-noticias"
        return self.buscar_conteudo(url)

    def extrair_url_noticias(self, dia_de, dia_ate) -> List[str]:
        retorno = []
        data_lista = dia_de.split('-')
        dia = data_lista[0]
        mes = data_lista[1]
        ano = data_lista[2]

        total_paginas = 1

        pagina_atual = 1
        while pagina_atual <= total_paginas:
            conteudo = self.buscar_noticias()

            if pagina_atual == 1:
                paginacao = conteudo.find("li", class_="pager-last").find("a")
                if paginacao:
                    texto_paginacao = paginacao["href"]
                    if (texto_paginacao.split("=")[-1]).isnumeric():
                        total_paginas = int(texto_paginacao.split("=")[-1])

            ref_noticias = conteudo.find("div", class_="view-content").find_all("div", class_="row-dia")

            for item in ref_noticias:
                div_data = item.find("div", class_=f"{dia}{mes}{ano} lista-noticias")
                if div_data:
                    div_noticias = div_data.find_all("div", class_="grid-item col-xs-12 col-sm-6 col-md-4 col-lg-4")
                else:
                    continue
                for div in div_noticias:
                    link = div.find("a")["href"]
                    retorno.append(link)

            pagina_atual += 1

        return retorno

    def extrair_noticias(self, url_noticias) -> List[NoticiaExtraida]:
        resultado = []
        for url in url_noticias:
            conteudo = self.buscar_conteudo(url).find("article")

            cabecalho_div = conteudo.find("header")

            titulo_div = cabecalho_div.find("h1")
            titulo = ""
            if titulo_div:
                titulo = titulo_div.text

            data_div = cabecalho_div.find("div", class_="date-in-parts")
            data_formatada = None
            if data_div:
                dia = int(data_div.find("span", class_="day").text)
                mes_str = data_div.find("span", class_="month").text
                ano = int(data_div.find("span", class_="year").text.replace("-", ""))

                data_formatada = date(ano, mapa_meses[mes_str], dia)

            url_imagem = ""
            div_primeira_imagem = cabecalho_div.find("img")
            if div_primeira_imagem:
                url_imagem = div_primeira_imagem["src"]

            conteudo_divs = conteudo.find("div", class_="field-items").find("div", class_="field-item even").find_all(True)
            conteudo_integral = ""
            for conteudo_div in conteudo_divs:
                if conteudo_div.name != "em":
                    conteudo_texto = conteudo_div.text
                    conteudo_integral += f"{conteudo_texto}\n"

            noticia_extraida = NoticiaExtraida(
                url_completa=url,
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
