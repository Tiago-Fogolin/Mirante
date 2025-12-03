import sys
import os
from datetime import date

# Adiciona o diretório raiz ao path para importar o 'app' corretamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.noticia import Noticia
from crawler.noticia_crawler.noticias_marilia_crawler import NoticiasMariliaCrawler

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
    crawler = NoticiasMariliaCrawler("https://www.marilia.sp.gov.br")
    lista_noticias_extraidas = crawler.rodar_crawler(data_inicio, data_fim)

    if not lista_noticias_extraidas:
        print("Nenhuma notícia encontrada no período.")
        return

    # 3. Salvar no Banco de Dados
    db = SessionLocal()
    contagem_novas = 0

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
                    url_imagem=item.url_imagem
                )
                db.add(nova_noticia)
                contagem_novas += 1
            else:
                print(f"Pular (já existe): {item.titulo[:30]}...")


        db.commit()
        print(f"\nSucesso! {contagem_novas} novas notícias salvas.")

    except Exception as e:
        print(f"Erro ao salvar no banco: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    main()
