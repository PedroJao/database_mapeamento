# 🗂️ Projeto de Mapeamento "De-Para": SAS x FOCO

Este é um projeto Django simples para criar um banco de dados "De-Para" (mapeamento) entre o sistema legado SAS e o novo sistema FOCO (Salesforce).

O projeto é totalmente containerizado com Docker e Docker Compose, utilizando `uv` para gerenciamento de pacotes.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Django
* **Banco de Dados:** PostgreSQL
* **Containerização:** Docker & Docker Compose
* **Servidor WSGI:** Gunicorn
* **Arquivos Estáticos:** Whitenoise
* **Gerenciador de Pacotes:** `uv`

## 🚀 Como Rodar o Projeto

Siga os passos abaixo para executar o projeto em um novo ambiente.

### Pré-requisitos

* [Docker](https://www.docker.com/get-started)
* [Docker Compose](https://docs.docker.com/compose/install/)
* Git

### 1. Preparação do Ambiente

Primeiro, clone o repositório e configure o arquivo de ambiente.

```bash
# 1. Clone o repositório (substitua pela URL do seu repo)
git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)

# 2. Entre na pasta do projeto
cd mapeamento_sas_foco

# 3. Copie o arquivo de exemplo .env-sample para .env
# O .env é ignorado pelo Git e contém seus segredos
cp .env-sample .env
Após o passo 3, você pode editar o arquivo .env se precisar alterar a senha padrão do banco de dados.

2. Executando o Projeto
Com os arquivos no lugar, suba os contêineres e configure o banco de dados.

Bash

# 1. Suba os serviços (app e db)
# O --build é importante na primeira vez
docker-compose up --build -d

# 2. Crie os arquivos de migração (MUITO IMPORTANTE)
# Este comando lê seus models.py e cria as "instruções"
docker-compose exec app uv run python manage.py makemigrations mapeamento

# 3. Aplique as migrações no banco de dados
# Este comando executa as instruções e cria as tabelas
docker-compose exec app uv run python manage.py migrate

# 4. Crie um superusuário para acessar o Admin
docker-compose exec app uv run python manage.py createsuperuser
Siga as instruções no terminal para definir o nome de usuário e a senha do seu administrador.

3. Acesse a Aplicação
Seu projeto está no ar!

Painel Admin: http://localhost:8010/admin/

Aplicação (Base): http://localhost:8010/

⚙️ Comandos Úteis do Docker
Parar todos os contêineres:

Bash

docker-compose down
Ver os logs da aplicação (em tempo real):

Bash

docker-compose logs -f app
Executar um comando dentro do contêiner (ex: shell):

Bash

docker-compose exec app uv run python manage.py shell
Forçar a reconstrução das imagens (se mudar o Dockerfile):

Bash

docker-compose up --build -d
