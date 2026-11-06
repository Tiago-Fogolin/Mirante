"""
Apaga noticias de Ribeirao Preto, Santos e Americana num periodo, pra
reprocessar com os crawlers corrigidos (RP: site mudou o HTML e quebrou a
extracao, alem do filtro de data que so pegava um dia; Americana: dado
antigo sem imagem/com municipio_id errado antes do fix do seed).

Uso (dentro do container do backend no Portainer):
  docker exec -it mirante_web python scripts/limpar_noticias_rp_santos.py
      -> dry-run, so lista o que seria apagado

  docker exec -it mirante_web python scripts/limpar_noticias_rp_santos.py --confirm
      -> apaga de fato

Depois de apagar, rebusque com:
  docker exec -it mirante_web python -m crawler.main 06-07-2026 06-11-2026
"""
import os
import sys
from datetime import date

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.municipio import Municipio
from app.models.noticia import Noticia

DATA_INICIO = date(2026, 7, 6)
DATA_FIM = date(2026, 11, 6)
MUNICIPIOS = ["Ribeirão Preto", "Santos", "Americana"]


def main():
    confirmar = "--confirm" in sys.argv

    db = SessionLocal()
    try:
        municipio_ids = [
            m.id for m in db.query(Municipio).filter(Municipio.nome.in_(MUNICIPIOS)).all()
        ]
        if len(municipio_ids) != len(MUNICIPIOS):
            print(f"ERRO: nem todos os municipios {MUNICIPIOS} foram encontrados no banco.")
            return

        noticias = (
            db.query(Noticia)
            .filter(
                Noticia.municipio_id.in_(municipio_ids),
                Noticia.data_publicacao >= DATA_INICIO,
                Noticia.data_publicacao <= DATA_FIM,
            )
            .all()
        )

        print(f"Periodo: {DATA_INICIO} até {DATA_FIM}")
        print(f"Encontradas {len(noticias)} noticias de {MUNICIPIOS}:")
        for n in noticias:
            print(f"  [{n.id}] {n.data_publicacao} - {n.titulo[:70]}")

        if not noticias:
            print("Nada pra apagar.")
            return

        if not confirmar:
            print("\nDry-run (nada foi apagado). Rode de novo com --confirm pra apagar de verdade.")
            return

        for n in noticias:
            db.delete(n)
        db.commit()
        print(f"\n{len(noticias)} noticias apagadas.")

    finally:
        db.close()


if __name__ == "__main__":
    main()
