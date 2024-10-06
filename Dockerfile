FROM python:3.12

WORKDIR /app

# Instale o netcat (caso necessário)
RUN apt-get update && apt-get install -y netcat-openbsd

COPY . /app
RUN pip install -r requirements.txt

# Torne o script executável
RUN chmod +x entrypoint.sh

# Execute o script usando bash
ENTRYPOINT ["bash", "./entrypoint.sh"]
