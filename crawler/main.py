import sys
import os
from datetime import date

# Adiciona o diretório raiz ao path para importar o 'app' corretamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.noticia import Noticia
from crawler.noticia_crawler.noticias_marilia_crawler import NoticiasMariliaCrawler
from crawler.noticia_crawler.noticias_paulinia_crawler import NoticiasPauliniaCrawler
from crawler.noticia_crawler.noticias_ribeirao_preto_crawler import NoticiasRibeiraoPretoCrawler
from crawler.noticia_crawler.noticias_santos_crawler import NoticiasSantosCrawler
from app.redis_client import fila
from workers.noticia_worker import check_and_add_noticia
# TODO -> jogar funções de salvar no banco de dados para service

def main():
    if len(sys.argv) < 3:
        print("Erro: Faltam argumentos.")
        print("Uso: python main.py <data_inicio> <data_fim>")
        print("Exemplo: python main.py 01-11-2025 05-11-2025")
        return

    data_inicio = sys.argv[1]
    data_fim = sys.argv[2]

    print(f"Buscando notícias de {data_inicio} até {data_fim}...")
    crawler_marilia = NoticiasMariliaCrawler("https://www.marilia.sp.gov.br")
    crawler_paulinia = NoticiasPauliniaCrawler("https://www.paulinia.sp.gov.br")
    crawler_ribeirao_preto = NoticiasRibeiraoPretoCrawler("https://www.ribeiraopreto.sp.gov.br/portal/")
    crawler_santos = NoticiasSantosCrawler("https://www.santos.sp.gov.br")
    lista_noticias_extraidas = crawler_marilia.rodar_crawler(data_inicio, data_fim)
    lista_noticias_extraidas.extend(crawler_paulinia.rodar_crawler(data_inicio, data_fim))
    lista_noticias_extraidas.extend(crawler_ribeirao_preto.rodar_crawler(data_inicio, data_fim))
    lista_noticias_extraidas.extend(crawler_santos.rodar_crawler(data_inicio, data_fim))

    if not lista_noticias_extraidas:
        print("Nenhuma notícia encontrada no período.")
        return


    db = SessionLocal()

    try:
        print("Salvando no banco de dados...")

        for item in lista_noticias_extraidas:
            existe = db.query(Noticia).filter(Noticia.url_completa == item.url_completa).first()

            if not existe:
                nova_noticia = Noticia(
                    titulo=item.titulo,
                    data_publicacao=item.data_publicacao,
                    url_completa=item.url_completa,
                    conteudo_integral=item.conteudo_integral,
                    url_imagem=item.url_imagem,
                    municipio_id=item.municipio_id
                )

                db.add(nova_noticia)
                print("Adicionando:", nova_noticia.titulo)
                db.flush()
                
                fila.enqueue(check_and_add_noticia, nova_noticia.municipio_id)

            else:
                print(f"Pular (já existe): {item.titulo[:30]}...")

        print("Pendentes na sessão:", db.new)
        db.commit()
        print("Crawler finalizado")

    except Exception as e:
        db.rollback()
        print("ERRO:", e)
    finally:
        db.close()

if __name__ == "__main__":
    main()
