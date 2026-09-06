from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Municipio, ODS

def seed_db():
    db = SessionLocal()
    try:
        municipios_seed = [
            {"nome": "São Paulo", "uf": "SP", "latitude": -23.5505, "longitude": -46.6333},
            {"nome": "Marília", "uf": "SP", "latitude": -22.2139, "longitude": -49.9458},
            {"nome": "São Caetano do Sul", "uf": "SP", "latitude": -23.6226, "longitude": -46.5505},
            {"nome": "Paulínia", "uf": "SP", "latitude": -22.7614, "longitude": -47.1533},
            {"nome": "Jundiaí", "uf": "SP", "latitude": -23.1857, "longitude": -46.8978},
            {"nome": "Sorocaba", "uf": "SP", "latitude": -23.5015, "longitude": -47.4581},
            {"nome": "Ribeirão Preto", "uf": "SP", "latitude": -21.1704, "longitude": -47.8103},
            {"nome": "São José dos Campos", "uf": "SP", "latitude": -23.2237, "longitude": -45.9009},
            {"nome": "Bauru", "uf": "SP", "latitude": -22.3145, "longitude": -49.0587},
            {"nome": "Americana", "uf": "SP", "latitude": -22.7392, "longitude": -47.3314},
            {"nome": "Piracicaba", "uf": "SP", "latitude": -22.7343, "longitude": -47.6481},
            {"nome": "Santos", "uf": "SP", "latitude": -23.9618, "longitude": -46.3322},
            {"nome": "Campinas", "uf": "SP", "latitude": -22.9099, "longitude": -47.0626},
            {"nome": "São José do Rio Preto", "uf": "SP", "latitude": -20.8113, "longitude": -49.3758},
            {"nome": "Presidente Prudente", "uf": "SP", "latitude": -22.1276, "longitude": -51.3856}
        ]


        for dados in municipios_seed:
            municipio_existente = db.query(Municipio).filter(Municipio.nome == dados["nome"]).first()

            if not municipio_existente:
                novo_municipio = Municipio(
                    nome=dados["nome"],
                    uf=dados["uf"],
                    latitude=dados["latitude"],
                    longitude=dados["longitude"]
                )
                db.add(novo_municipio)
                print(f"Município {dados['nome']} criado e adicionado.")
            else:
                atualizou = False
                if municipio_existente.latitude != dados["latitude"]:
                    municipio_existente.latitude = dados["latitude"]
                    atualizou = True

                if municipio_existente.longitude != dados["longitude"]:
                    municipio_existente.longitude = dados["longitude"]
                    atualizou = True

                if atualizou:
                    print(f"Município {dados['nome']} atualizado com as coordenadas.")

        ods_data = [
            (1, "Erradicação da Pobreza"),
            (2, "Fome Zero e Agricultura Sustentável"),
            (3, "Saúde e Bem-Estar"),
            (4, "Educação de Qualidade"),
            (5, "Igualdade de Gênero"),
            (6, "Água Potável e Saneamento"),
            (7, "Energia Limpa e Acessível"),
            (8, "Trabalho Decente e Crescimento Econômico"),
            (9, "Indústria, Inovação e Infraestrutura"),
            (10, "Redução das Desigualdades"),
            (11, "Cidades e Comunidades Sustentáveis"),
            (12, "Consumo e Produção Responsáveis"),
            (13, "Ação Contra a Mudança Global do Clima"),
            (14, "Vida na Água"),
            (15, "Vida Terrestre"),
            (16, "Paz, Justiça e Instituições Eficazes"),
            (17, "Parcerias e Meios de Implementação")
        ]

        for numero, nome in ods_data:
            exists = db.query(ODS).filter(ODS.numero == numero).first()
            if not exists:
                nova_ods = ODS(numero=numero, nome=nome)
                db.add(nova_ods)

        db.commit()
        print("As 17 ODS foram verificadas/inseridas.")

    except Exception as e:
        print(f"❌ Erro ao semear banco: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
