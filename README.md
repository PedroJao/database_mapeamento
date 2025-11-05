🗂️ Projeto de Mapeamento "De-Para": SAS x FOCO
Uma aplicação Django simples para criar um banco de dados "De-Para" que documenta o mapeamento de campos entre o sistema legado SAS e o novo sistema FOCO (Salesforce).

O projeto é totalmente containerizado com Docker e Docker Compose, utilizando uv para gerenciamento de pacotes.

🛠️ Tecnologias Utilizadas
Backend: Django

Banco de Dados: PostgreSQL

Containerização: Docker & Docker Compose

Servidor WSGI: Gunicorn

Arquivos Estáticos: Whitenoise

Gerenciador de Pacotes: uv (da Astral)

✅ Pré-requisitos
Docker

Docker Compose

🚀 Rodando o Projeto Localmente
Siga estes passos para configurar e rodar a aplicação no seu ambiente local.

1. Clone o Repositório
Bash

git clone <url-do-seu-repositorio>
cd mapeamento_sas_foco
2. Crie o Arquivo de Ambiente (.env)
Crie um arquivo chamado .env na raiz do projeto. Este arquivo não é enviado para o Git e contém suas senhas.

Copie e cole o seguinte conteúdo nele:

Ini, TOML

# Variáveis de ambiente para o docker-compose

# Configs do Banco de Dados
POSTGRES_DB=sas_foco_db
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin

# Configs do Django (para conectar no DB)
DB_HOST=db
DB_PORT=5432
3. Suba os Contêineres
Este comando irá construir as imagens do Docker (se for a primeira vez) e iniciar os serviços da aplicação (app) e do banco de dados (db).

Bash

docker-compose up --build -d
4. Execute as Migrações do Banco
Com os contêineres rodando, precisamos criar as tabelas no banco de dados.

Bash

docker-compose exec app uv run python manage.py migrate
5. Crie um Superusuário
Você precisará de um usuário administrador para acessar o painel /admin do Django.

Bash

docker-compose exec app uv run python manage.py createsuperuser
Siga as instruções no terminal para criar seu usuário (nome, email e senha).

6. Pronto!
A aplicação está no ar!

Aplicação: http://localhost:8010/

Painel Admin: http://localhost:8010/admin/

Comandos Úteis do Docker
Parar os contêineres:

Bash

docker-compose down
Ver os logs da aplicação:

Bash

docker-compose logs -f app
Rodar um comando (ex: shell do Django):

Bash

docker-compose exec app uv run python manage.py shell