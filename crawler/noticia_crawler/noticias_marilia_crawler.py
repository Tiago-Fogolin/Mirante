from crawler.noticia_crawler.noticias_crawler import *
import requests
from bs4 import BeautifulSoup
from datetime import date

mapa_meses = {
    'JAN': 1, 'FEV': 2, 'MAR': 3, 'ABR': 4, 'MAI': 5, 'JUN': 6,
    'JUL': 7, 'AGO': 8, 'SET': 9, 'OUT': 10, 'NOV': 11, 'DEZ': 12
}

class NoticiasMariliaCrawler():
    def __init__(self, base_url):
        self.base_url = base_url

    def buscar_conteudo(self, url) -> BeautifulSoup:
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def buscar_noticias(self, dia_de, dia_ate, pagina=1) -> BeautifulSoup:
        url = self.base_url + f"/portal/noticias/3/{pagina}/0/{dia_de}/{dia_ate}/0"
        return self.buscar_conteudo(url)

    def extrair_url_noticias(self, dia_de, dia_ate) -> List[str]:
        retorno = []

        total_paginas = 1

        pagina_atual = 1
        while pagina_atual <= total_paginas:
            conteudo = self.buscar_noticias(dia_de, dia_ate)

            if pagina_atual == 1:
                tool_tip_paginacao = conteudo.find("div", class_="sw_cont_paginacao sw_txt_tooltip")
                if tool_tip_paginacao:
                    texto_paginacao_dividido = tool_tip_paginacao["title"].split()
                    if (texto_paginacao_dividido[-1]).isnumeric():
                        total_paginas = int(texto_paginacao_dividido[-1])


            ref_noticias = conteudo.find("div", class_="ntc_cont_noticias").find_all("a")

            for item in ref_noticias:
                retorno.append(item["href"])

            pagina_atual += 1


        return retorno

    def extrair_noticias(self, url_noticias) -> List[NoticiaExtraida]:
        resultado = []
        for url in url_noticias:
            conteudo = self.buscar_conteudo(self.base_url + url)

            # TODO -> parsear essa data
            data_div = conteudo.find("div", class_="ntc_data_noticia sw_lato")
            data_raw = ""
            data_formatada = None
            if data_div:
                data_raw = data_div.text
                partes = data_raw.split()
                dia = int(partes[0])
                mes_str = partes[1].upper()
                ano = int(partes[2])

                data_formatada = date(ano, mapa_meses[mes_str], dia)

            titulo_div = conteudo.find("div", class_="ntc_titulo_noticia sw_lato_bold sw_leitura_audio")
            titulo = ""
            if titulo_div:
                titulo = titulo_div.text

            conteudo_div = conteudo.find("div", class_="ntc_cont_descricao_noticia sw_txteditor")
            conteudo_integral = ""
            if conteudo_div:
                conteudo_integral = conteudo_div.text

            url_imagem = ""
            div_primeira_imagem = conteudo.find(
                "div",
                class_="ntc_thumbnail_imagem_noticia"
            )

            if div_primeira_imagem:
                tag_imagem = div_primeira_imagem.find("a")
                if tag_imagem:
                    url_imagem = tag_imagem["href"]



            noticia_extraida = NoticiaExtraida(
                url_completa=self.base_url + url,
                data_publicacao=data_formatada,
                titulo=titulo,
                conteudo_integral=conteudo_integral,
                url_imagem=self.base_url + url_imagem
            )

            resultado.append(noticia_extraida)

        return resultado

    def rodar_crawler(self, dia_de: str, dia_ate: str):

        urls = self.extrair_url_noticias(dia_de, dia_ate)
        noticias = self.extrair_noticias(urls)

        return noticias


t = NoticiasMariliaCrawler("https://www.marilia.sp.gov.br")
noticias = t.rodar_crawler("01-11-2025", "01-11-2025")
print(noticias)
