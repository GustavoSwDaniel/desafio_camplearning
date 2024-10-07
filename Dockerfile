FROM python:3.12

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-openbsd

COPY . /app
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

ENTRYPOINT ["bash", "./entrypoint.sh"]
