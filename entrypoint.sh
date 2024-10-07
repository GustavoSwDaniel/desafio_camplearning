#!/bin/bash
while ! nc -z db 5432; do
  echo "Aguardando o banco de dados estar disponível..."
  sleep 0.1
done

echo "Aplicando migrações do Django..."
python manage.py migrate

echo "Verificando se o superusuário já existe..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(email='admin@example.com').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superusuário criado.")
else:
    print("Superusuário já existe.")
EOF

echo "Iniciando o servidor Django..."
python manage.py runserver 0.0.0.0:8000
