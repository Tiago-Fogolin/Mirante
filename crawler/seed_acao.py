from datetime import date
from app.database import SessionLocal
from app.models.acao import Acao, StatusAcaoEnum
from app.models.acao_ods import AcaoOds
from app.models.municipio import Municipio
from app.models.ods import ODS
from app.models.tema import Tema


def seed_acoes():
    db = SessionLocal()
    try:
        acoes_seed = [
            {
                "nome_organizacao": "Cooperativa Rural Sol Nascente",
                "email_contato": "contato@cooperativasol.org.br",
                "telefone_contato": "(11) 92222-3333",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Feira de Agricultura Familiar",
                "data_inicio": date(2025, 12, 27),
                "data_fim": None,
                "descricao": "Feira semanal para produtores rurais locais venderem direto ao consumidor.",
                "publico_alvo": "Produtores rurais",
                "financiador": "Secretaria de Agricultura",
                "objetivos": "Fomentar a economia local e consumo sustentável",
                "possui_vinculo": True,
                "participa_conselhos": False,
                "usa_dados_abertos": False,
                "municipio_nome": "Marília",
                "temas": ["Agricultura Sustentável"],
                "ods": [1, 2, 8],
            },
            {
                "nome_organizacao": "Associação de Moradores da Bacia",
                "email_contato": "contato@bairropri.org.br",
                "telefone_contato": "(11) 98765-4321",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Horta Comunitária no Bairro Primavera",
                "data_inicio": date(2026, 2, 5),
                "data_fim": None,
                "descricao": "Implementação de horta comunitária para provisão de alimentos orgânicos, fortalecendo a segurança alimentar local.",
                "publico_alvo": "Moradores locais",
                "financiador": "Fundo Municipal de Meio Ambiente",
                "objetivos": "Garantir segurança alimentar e educação ambiental",
                "possui_vinculo": True,
                "participa_conselhos": True,
                "usa_dados_abertos": False,
                "municipio_nome": "Marília",
                "temas": ["Agricultura Sustentável"],
                "ods": [2],
            },
            {
                "nome_organizacao": "Tech Sustentável LTDA",
                "email_contato": "reciclagem@techsustentavel.com.br",
                "telefone_contato": "(11) 91234-5678",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Programa de Reciclagem de Eletrônicos",
                "data_inicio": date(2026, 3, 21),
                "data_fim": None,
                "descricao": "Ponto de coleta e destinação correta de lixo eletrônico na cidade, promovendo a economia circular.",
                "publico_alvo": "População em geral",
                "financiador": "Iniciativa Privada",
                "objetivos": "Reduzir o impacto ambiental do lixo eletrônico",
                "possui_vinculo": False,
                "participa_conselhos": True,
                "usa_dados_abertos": True,
                "municipio_nome": "Marília",
                "temas": ["Meio Ambiente"],
                "ods": [11, 15],
            },
            {
                "nome_organizacao": "ONG Vida Saudável",
                "email_contato": "atendimento@ongvidasaudavel.org.br",
                "telefone_contato": "(11) 99876-5432",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Mutirão de Saúde Preventiva",
                "data_inicio": date(2026, 3, 29),
                "data_fim": None,
                "descricao": "Atendimento médico e odontológico gratuito para famílias de baixa renda e comunidades vulneráveis.",
                "publico_alvo": "Famílias de baixa renda",
                "financiador": "Fundação Saúde & Vida",
                "objetivos": "Aumentar a acessibilidade a serviços básicos de saúde",
                "possui_vinculo": True,
                "participa_conselhos": False,
                "usa_dados_abertos": True,
                "municipio_nome": "Marília",
                "temas": ["Saúde Pública"],
                "ods": [3],
            },
            {
                "nome_organizacao": "Instituto Futuro Digital",
                "email_contato": "cursos@futurodigital.org.br",
                "telefone_contato": "(11) 97654-3210",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Capacitação em Programação para Jovens",
                "data_inicio": date(2026, 1, 31),
                "data_fim": None,
                "descricao": "Aulas de python e desenvolvimento web para jovens de escolas públicas, visando a inserção no mercado de trabalho.",
                "publico_alvo": "Jovens e adolescentes",
                "financiador": "Banco de Desenvolvimento Regional",
                "objetivos": "Proporcionar capacitação técnica para inserção no mercado tech",
                "possui_vinculo": False,
                "participa_conselhos": True,
                "usa_dados_abertos": True,
                "municipio_nome": "Marília",
                "temas": ["Tecnologia e Inovação"],
                "ods": [4, 8],
            },
            {
                "nome_organizacao": "Coletivo Águas Limpas",
                "email_contato": "contato@aguaslimpas.org.br",
                "telefone_contato": "(14) 95555-4444",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Limpeza do Rio do Peixe",
                "data_inicio": date(2026, 3, 5),
                "data_fim": None,
                "descricao": "Ação voluntária para retirada de resíduos sólidos das margens do rio local e conscientização ambiental.",
                "publico_alvo": "Comunidade local",
                "financiador": "Agência Nacional de Águas",
                "objetivos": "Revitalizar o ecossistema fluvial",
                "possui_vinculo": True,
                "participa_conselhos": False,
                "usa_dados_abertos": False,
                "municipio_nome": "Marília",
                "temas": ["Meio Ambiente"],
                "ods": [6, 11, 15],
            },
            {
                "nome_organizacao": "Banco da Mulher Inovadora",
                "email_contato": "apoio@bancomulher.org.br",
                "telefone_contato": "(11) 96325-8741",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Apoio a Mulheres Empreendedoras",
                "data_inicio": date(2026, 4, 1),
                "data_fim": None,
                "descricao": "Microcrédito e mentoria para mulheres chefes de família ampliarem seus negócios locais.",
                "publico_alvo": "Mulheres empreendedoras",
                "financiador": "Fundo da Mulher Empreendedora",
                "objetivos": "Empoderar e dar independência financeira para mulheres",
                "possui_vinculo": False,
                "participa_conselhos": False,
                "usa_dados_abertos": True,
                "municipio_nome": "Marília",
                "temas": ["Direitos Humanos"],
                "ods": [1, 5, 8],
            },
            {
                "nome_organizacao": "Associação Cultural Mosaico",
                "email_contato": "cine@culturalmosaico.org.br",
                "telefone_contato": "(11) 91111-2222",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Cineclube Cidadania",
                "data_inicio": date(2026, 3, 6),
                "data_fim": None,
                "descricao": "Exibição de filmes e debates em praças públicas de bairros periféricos.",
                "publico_alvo": "Comunidades periféricas",
                "financiador": "Edital Municipal de Cultura",
                "objetivos": "Democratizar o acesso à cultura e fomentar a socialização",
                "possui_vinculo": False,
                "participa_conselhos": False,
                "usa_dados_abertos": False,
                "municipio_nome": "Marília",
                "temas": ["Cultura e Lazer"],
                "ods": [11, 16],
            },
            {
                "nome_organizacao": "Secretaria de Mobilidade Ativa",
                "email_contato": "mobilidade@smt.gov.br",
                "telefone_contato": "(11) 3232-4455",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Implementação de Ciclovias Inclusivas",
                "data_inicio": date(2026, 1, 18),
                "data_fim": None,
                "descricao": "Projeto de mobilidade urbana com foco em segurança para ciclistas e incentivo ao uso da bicicleta.",
                "publico_alvo": "Ciclistas urbanos",
                "financiador": "Banco Interamericano de Desenvolvimento",
                "objetivos": "Fornecer infraestrutura segura para ciclistas",
                "possui_vinculo": False,
                "participa_conselhos": True,
                "usa_dados_abertos": True,
                "municipio_nome": "Marília",
                "temas": ["Mobilidade Urbana"],
                "ods": [11],
            },
            {
                "nome_organizacao": "Instituto Amigos da Árvore",
                "email_contato": "plantio@amigosarvore.org.br",
                "telefone_contato": "(11) 99999-8888",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Reflorestamento de Áreas Degradadas",
                "data_inicio": date(2026, 1, 11),
                "data_fim": None,
                "descricao": "Plantio de mil mudas nativas em áreas de preservação ambiental da cidade.",
                "publico_alvo": "Meio ambiente",
                "financiador": "Ministério do Meio Ambiente",
                "objetivos": "Recuperar a biodiversidade local",
                "possui_vinculo": True,
                "participa_conselhos": True,
                "usa_dados_abertos": False,
                "municipio_nome": "Marília",
                "temas": ["Meio Ambiente"],
                "ods": [13, 15],
            },
            {
                "nome_organizacao": "Observatório Social Metropolitano",
                "email_contato": "contato@observatorio.org.br",
                "telefone_contato": "(11) 97777-6666",
                "status": StatusAcaoEnum.NAO_INICIADA,
                "titulo": "Plataforma de Transparência Pública",
                "data_inicio": date(2026, 3, 21),
                "data_fim": None,
                "descricao": "Criação de portal de dados abertos sobre os gastos do município para consulta da população.",
                "publico_alvo": "Cidadãos",
                "financiador": "Fundo de Combate à Corrupção",
                "objetivos": "Aumentar o controle social sobre o orçamento público",
                "possui_vinculo": True,
                "participa_conselhos": True,
                "usa_dados_abertos": True,
                "municipio_nome": "Marília",
                "temas": ["Gestão Pública"],
                "ods": [16],
            },
            {
                "nome_organizacao": "Centro Comunitário Viva Vida",
                "sigla_organizacao": "ASV",
                "documento_ator": "12.345.678/0001-99",
                "tipo_ator": "Sociedade Civil (OSC)",
                "ano_fundacao": 2018,
                "website": "www.semeandovida.org.br",
                "email_contato": "oficinas@vivavida.org.br",
                "telefone_contato": "(11) 98888-7777",
                "abrangencia_geografica": "Zona Periférica Norte e arredores de escolas públicas",
                "status": StatusAcaoEnum.EM_ANDAMENTO,
                "titulo": "Oficina de Geração de Renda: Artesanato",
                "data_inicio": date(2026, 2, 19),
                "data_fim": date(2025, 12, 20),
                "descricao": "Cursos de artesanato com materiais recicláveis voltados para a terceira idade.",
                "publico_alvo": "Idosos",
                "numero_colaboradores": 12,
                "financiador": "Assistência Social Municipal",
                "objetivos": "Estimular a autonomia financeira e saúde mental",
                "resultados_esperados": "Produzir 5 toneladas de alimentos orgânicos por ano; Reduzir a insegurança alimentar de 300 famílias locais; Capacitar 50 jovens em técnicas de agricultura urbana e economia solidária.",
                "resultados_alcancados": "Revitalização de 3 terrenos que eram pontos de descarte irregular de lixo; Primeira colheita de 500kg de hortaliças distribuída para o banco de alimentos municipal.",
                "aprendizados_inovacoes": "Desenvolvimento de um sistema de irrigação automatizada de baixo custo utilizando materiais reciclados e captação de água da chuva.",
                "parcerias_envolvidas": "Secretaria Municipal de Meio Ambiente, Escola Técnica Estadual e Cooperativa de Reciclagem Local.",
                "possui_vinculo": False,
                "vinculo_politica_publica": "Plano Municipal de Segurança Alimentar e Nutricional",
                "participa_conselhos": False,
                "participacao_conselhos": "Conselho Municipal de Segurança Alimentar (COMSEA)",
                "usa_dados_abertos": False,
                "tecnologias_utilizadas": "Compostagem termofílica, cisternas de captação pluvial e aplicativo para gestão da distribuição de cestas.",
                "indicadores_impacto": "Quilos de alimentos produzidos, Número de famílias beneficiadas, Toneladas de resíduos orgânicos compostados.",
                "observacoes": "O projeto serve como modelo piloto para replicação em outros bairros.",
                "municipio_nome": "Marília",
                "temas": ["Desenvolvimento Econômico"],
                "ods": [1, 4, 11],
            },
        ]

        for dados in acoes_seed:
            existente = (
                db.query(Acao)
                .filter(Acao.titulo == dados["titulo"], Acao.nome_organizacao == dados["nome_organizacao"])
                .first()
            )
            if existente:
                print(f"Ação '{dados['titulo']}' já existe, pulando.")
                continue

            municipio = db.query(Municipio).filter(Municipio.nome == dados["municipio_nome"]).first()
            if not municipio:
                print(f"Município '{dados['municipio_nome']}' não encontrado, pulando ação '{dados['titulo']}'.")
                continue

            temas_objs = []
            for nome_tema in dados.get("temas", []):
                tema = db.query(Tema).filter(Tema.nome == nome_tema).first()
                if not tema:
                    tema = Tema(nome=nome_tema, descricao=f"Ações relacionadas a {nome_tema}")
                    db.add(tema)
                    db.flush()
                temas_objs.append(tema)

            campos_excluidos = {"municipio_nome", "temas", "ods"}
            acao_kwargs = {k: v for k, v in dados.items() if k not in campos_excluidos}
            acao_kwargs["municipio_id"] = municipio.id

            nova_acao = Acao(**acao_kwargs)
            nova_acao.temas = temas_objs
            db.add(nova_acao)
            db.flush()

            for numero_ods in dados.get("ods", []):
                ods_obj = db.query(ODS).filter(ODS.numero == numero_ods).first()
                if not ods_obj:
                    print(f"ODS número {numero_ods} não encontrado, pulando vínculo.")
                    continue
                db.add(AcaoOds(acao_id=nova_acao.id, ods_id=ods_obj.id))

            print(f"Ação '{dados['titulo']}' criada.")

        db.commit()
        print("Seed de ações concluído.")
    except Exception as e:
        print(f"❌ Erro ao semear ações: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_acoes()
