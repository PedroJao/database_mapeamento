Passo a passo 

cd mapeamento_sas_foco

POSTGRES_DB=sas_foco_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin

DB_HOST=db
DB_PORT=5432

Para rodar:

docker-compose up --build -d

Bash (Para criar o superusuario, com docker rodando)

docker-compose exec app uv run python manage.py makemigrations mapeamento

docker-compose exec app uv run python manage.py migrate

docker-compose exec app uv run python manage.py createsuperuser

Aplicação: http://localhost:8010/

Painel Admin: http://localhost:8010/admin/

