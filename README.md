Rodar fastapi:
- uvicorn app.main:app --reload

Criar migration:
- alembic revision --autogenerate -m "nome_migration"

Aplicar migration:
- alembic upgrade head