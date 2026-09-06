from crawler.noticia_crawler.noticias_crawler import *
import requests
from bs4 import BeautifulSoup
from datetime import date

mapa_meses = {
    'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
    'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12
}

class NoticiasRibeiraoPretoCrawler():
    def __init__(self, base_url):
        self.base_url = base_url
        self.municipio_id = 3

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
                link = item.find("td").find("a")["href"]
                retorno.append(link)

            pagina_atual += 1

        return retorno

    def extrair_noticias(self, url_noticias) -> List[NoticiaExtraida]:
        resultado = []
        for url in url_noticias:
            conteudo = self.buscar_conteudo(self.base_url + url).find("section")
            # /html/body/div[1]/div[1]/div/section/text()

            h2 = conteudo.find("h2")
            titulo = ""
            if h2:
                titulo = h2.text

            data_texto = ""
            for node in h2.previous_siblings:
                if isinstance(node, str) and node.strip():
                    data_texto = node.strip()[:10]
                    break
            # data_texto = conteudo.find("/html/body/div[1]/div[1]/div/section/text()").text
            data_formatada = None
            if data_texto:
                partes = data_texto.split("/")
                dia = int(partes[0])
                mes = int(partes[1])
                ano = int(partes[2])

                data_formatada = date(ano, mes, dia)


            conteudo_divs = conteudo.find_all("p", style_= "text-align:justify")
            conteudo_integral = ""
            for conteudo_div in conteudo_divs:
                conteudo_span = conteudo_div.find("span", style_="font-size:16px")
                if conteudo_span:
                    conteudo_texto = conteudo_span.text
                    conteudo_integral += f"{conteudo_texto}\n"

            url_imagem = ""
            div_primeira_imagem = conteudo.find("img")
            if div_primeira_imagem:
                url_imagem = div_primeira_imagem["src"]

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
