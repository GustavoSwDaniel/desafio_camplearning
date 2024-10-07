
# File Management System with AWS S3

Este é um sistema simples de gerenciamento de arquivos, onde os usuários podem fazer upload de arquivos que são armazenados no **AWS S3**. Cada usuário tem acesso apenas aos seus próprios arquivos. O sistema é construído em **Django** e utiliza um banco de dados **PostgreSQL**. Ele foi projetado para ser facilmente executado em contêineres **Docker**.

## Funcionalidades

- Upload e gerenciamento de arquivos para cada usuário individualmente.
- Armazenamento seguro de arquivos no **Amazon S3**.
- Usuários podem acessar apenas seus próprios arquivos.
- Sistema fácil de configurar e rodar com Docker.

## Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado em seu ambiente:

- Docker
- Docker Compose

## Variáveis de Ambiente

Você precisa configurar um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente (substitua os valores da AWS pelas suas próprias credenciais e detalhes):

```bash
AWS_ACCESS_KEY_ID=SEU_ACCESS_KEY
AWS_SECRET_ACCESS_KEY=SUA_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=SEU_BUCKET_NAME
AWS_S3_REGION_NAME=SUA_REGION

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=SUA_SENHA
```

> **Nota:** Certifique-se de **NÃO compartilhar** suas credenciais da AWS em nenhum lugar público, como este exemplo.

## Como rodar o projeto

Siga os passos abaixo para rodar o projeto em um ambiente Docker:

1. Clone o repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/GustavoSwDaniel/desafio_camplearning.git
   cd seu-repositorio
   ```

2. Crie o arquivo `.env` conforme descrito acima.

3. Construa e rode os contêineres Docker:
   ```bash
   docker-compose up -d --build
   ```

4. O sistema criará automaticamente um superusuário com as seguintes credenciais:
   - **Email:** `admin@exemplo.com`
   - **Senha:** `admin`

   Você pode usar essas credenciais para acessar a interface de administração do Django e gerenciar usuários e arquivos.

## Para rodar os teste unitarios 
   Roda os seguinte comandos 
 ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   python manage.py test
   ```

## Acessando o sistema

- O sistema estará disponível em: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Acesse a interface de administração em: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Estrutura do projeto

- **Django** para a lógica de backend e autenticação de usuários.
- **AWS S3** para armazenamento de arquivos.
- **PostgreSQL** como banco de dados para armazenar informações de usuários e arquivos.
- **Docker** para facilitar a configuração e execução do ambiente de desenvolvimento e produção.



## Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Licença

Este projeto é licenciado sob a MIT License. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
