from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models import Municipio, ODS

def seed_db():
    db = SessionLocal()
    try:
        marilia = db.query(Municipio).filter(Municipio.nome == "Marília").first()
        if not marilia:
            marilia = Municipio(
                nome="Marília",
                uf="SP"
            )
            db.add(marilia)
            print("Município Marília adicionado.")

        paulinia = db.query(Municipio).filter(Municipio.nome == "Paulínia").first()
        if not paulinia:
            paulinia = Municipio(
                nome="Paulínia",
                uf="SP"
            )
            db.add(paulinia)
            print("Município Paulínia adicionado.")

        ribeirao_preto = db.query(Municipio).filter(Municipio.nome == "Ribeirão Preto").first()
        if not ribeirao_preto:
            ribeirao_preto = Municipio(
                nome="Ribeirão Preto",
                uf="SP"
            )
            db.add(ribeirao_preto)
            print("Município Ribeirão Preto adicionado.")

        santos = db.query(Municipio).filter(Municipio.nome == "Santos").first()
        if not santos:
            santos = Municipio(
                nome="Santos",
                uf="SP"
            )
            db.add(santos)
            print("Município Santos adicionado.")

        americana = db.query(Municipio).filter(Municipio.nome == "Americana").first()
        if not americana:
            americana = Municipio(
                nome="Americana",
                uf="SP"
            )
            db.add(americana)
            print("Município Americana adicionado.")

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
