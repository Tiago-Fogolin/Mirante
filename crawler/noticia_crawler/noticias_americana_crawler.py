from crawler.noticia_crawler.noticias_crawler import *
import requests
import urllib3
from bs4 import BeautifulSoup
from datetime import date, datetime

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

mapa_meses = {
    'Janeiro': 1, 'Fevereiro': 2, 'Março': 3, 'Abril': 4, 'Maio': 5, 'Junho': 6,
    'Julho': 7, 'Agosto': 8, 'Setembro': 9, 'Outubro': 10, 'Novembro': 11, 'Dezembro': 12
}

class NoticiasAmericanaCrawler():
    def __init__(self, base_url):
        self.base_url = base_url
        self.municipio_id = 5

    def buscar_conteudo(self, url) -> BeautifulSoup:
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def buscar_noticias(self) -> BeautifulSoup:
        url = self.base_url + "americana-index.php?a=noticias"
        return self.buscar_conteudo(url)

    def extrair_url_noticias(self, dia_de, dia_ate) -> List[str]:
        retorno = []

        dia_de_formatado = datetime.strptime(dia_de, "%d-%m-%Y").date()
        dia_ate_formatado = datetime.strptime(dia_ate, "%d-%m-%Y").date()

        total_paginas = 1

        pagina_atual = 1
        while pagina_atual <= total_paginas:
            conteudo = self.buscar_noticias()

            ref_datas_noticias = conteudo.find("div", class_="card card-body border-0 px-4 py-4")
            # ref_datas = ref_datas_noticias.find_all("div", class_=r"font-titulo-1 fw-bold mt-[23] mb-1")
            ref_datas = ref_datas_noticias.select("div.font-titulo-1.fw-bold.mb-1")
            ref_noticias = ref_datas_noticias.find_all("ul", class_="list-unstyled mb-0")

            for i in range(len(ref_datas)):
                div_data_texto = ref_datas[i].text
                data_texto = (div_data_texto[(div_data_texto.find(",") + 1):].strip()
                              .replace("de ", ""))
                print(f"data_texto: {data_texto}")
                data_lista = data_texto.split()
                dia = int(data_lista[0])
                mes_str = data_lista[1]
                ano = int(data_lista[2])
                data_formatada = date(ano, mapa_meses[mes_str], dia)

                if dia_de_formatado <= data_formatada <= dia_ate_formatado:
                    lista_noticias = ref_noticias[i].find_all("li", class_="lh-sm pb-2")
                else:
                    continue

                for item in lista_noticias:
                    retorno.append(item.find("a")["href"])

            pagina_atual += 1

        return retorno

    def extrair_noticias(self, url_noticias) -> List[NoticiaExtraida]:
        resultado = []
        for url in url_noticias:
            conteudo = (self.buscar_conteudo(self.base_url + url)
                        .find("div", class_="card card-body mb-4 border-0 px-4 py-4 px-lg-5"))

            data_div = conteudo.find("div", class_="h6 pt-2")
            data_raw = ""
            data_formatada = None
            if data_div:
                data_raw = (data_div.text.split("em ")[1].split(" às")[0].strip()
                            .replace("de ", ""))
                partes = data_raw.split()
                dia = int(partes[0])
                mes_str = partes[1]
                ano = int(partes[2])
                data_formatada = date(ano, mapa_meses[mes_str], dia)

            titulo_div = conteudo.find("h1")
            titulo = ""
            if titulo_div:
                titulo = titulo_div.text

            conteudo_div = conteudo.find("div", class_="mb-5")
            conteudo_integral = ""
            if conteudo_div:
                conteudo_integral = conteudo_div.text

            url_imagem = ""
            div_primeira_imagem = conteudo.find("img")
            if div_primeira_imagem:
                url_imagem = self.base_url + div_primeira_imagem["src"]

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
