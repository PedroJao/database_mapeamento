FROM alpine:3.22.2

# --- MUDANÇA PRINCIPAL ---
# 1. Instale python3, as ferramentas de 'dev' (para compilar pacotes) e o 'build-base'
# 2. Crie um link simbólico (symlink) para que o comando 'python' aponte para 'python3'
RUN apk add --no-cache python3 python3-dev build-base tzdata && ln -sf /usr/bin/python3 /usr/bin/python

# Copie o 'uv'
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /source

# Copie os arquivos de dependência
COPY ./pyproject.toml /source/pyproject.toml
COPY ./uv.lock /source/uv.lock

# Instale as dependências
# Agora 'uv sync' encontrará 'python' e as ferramentas de build
RUN uv sync --no-dev

# Copie o código-fonte do Django
COPY ./src /source/src

# Variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Mude o diretório de trabalho para onde o código está
WORKDIR /source/src

# Diga ao Django para coletar todos os arquivos estáticos (CSS, JS)
RUN uv run python manage.py collectstatic --noinput

# Exponha a porta 8010
EXPOSE 8010

# O CMD agora usará 'python' (que agora é python3)
CMD ["uv", "run", "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8010"]